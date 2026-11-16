const roleList = document.getElementById("role-list");
const searchInput = document.getElementById("search");
const searchClear = document.getElementById("search-clear");
const categoryFilter = document.getElementById("category-filter");
const resultCount = document.getElementById("result-count");
const roleCountEl = document.getElementById("role-count");
const loadMoreBtn = document.getElementById("load-more");

// Matches PAGE_SIZE in scripts/build_pages.py — the SSR'd homepage ships this
// many cards up front (real content for no-JS / crawlers), everything past
// it exists only in data/roles.json and renders on "Load more". Keeps the
// live DOM off Lighthouse's excessive-DOM-size line instead of shipping and
// re-rendering all ~950 cards on every load.
const PAGE_SIZE = 60;

let roles = [];
let activeCategory = "";
let shownCount = PAGE_SIZE;

function cardHtml(r) {
  return `
    <a class="role-card" href="roles/${r.slug}/">
      <h3>${escapeHtml(titleCase(r.slug))}</h3>
      <div class="badges">
        <span class="badge">${escapeHtml(r.category)}</span>
        <span class="badge status-${r.status}">${escapeHtml(r.status)}</span>
      </div>
      <p>${escapeHtml(r.description)}</p>
    </a>
  `;
}

// Same filler words and plural stemming as `npx domain-experts match`
// (bin/cli.js STOPWORDS / stem), so a query typed the way the hero shows
// ("i need a contract lawyer") finds roles here too. Keep the two in sync.
const STOPWORDS = new Set([
  "a", "an", "the", "for", "of", "to", "in", "on", "and", "or", "with",
  "my", "me", "i", "need", "want", "act", "as", "like", "help", "who",
  "job", "role", "expert", "someone", "person",
  "how", "much", "many", "do", "does", "did", "have", "has", "having",
  "had", "left", "should", "shall", "would", "could", "can", "will",
  "we", "us", "our", "you", "your", "let", "lets", "get", "give",
  "tell", "please", "this", "that", "these", "those", "is", "are",
  "was", "were", "be", "been", "being", "it", "its", "at", "by", "from",
  "about", "into", "over", "than", "then", "so", "if", "not", "no",
  "what", "when", "where", "which", "why", "just", "really", "some",
  "any", "all", "one", "out", "up", "down", "now",
]);

function stem(word) {
  if (word.length <= 4) return word;
  if (word.endsWith("ies")) return word.slice(0, -3) + "y";
  if (/[sxz]es$|[cs]hes$/.test(word)) return word.slice(0, -2);
  if (word.endsWith("s") && !word.endsWith("ss")) return word.slice(0, -1);
  return word;
}

// Every remaining word must appear somewhere in the role (any order), so
// "contract lawyer" and "lawyer contract" both work. A word matches as typed
// or stemmed ("nurses" finds "nurse", "studies" still finds "studies").
// A query made only of filler words (or of single letters, as "c++" becomes)
// falls back to a plain substring match. Each term is a list of forms.
function queryTerms(q) {
  const terms = q
    .replace(/[^a-z0-9\s-]/g, " ")
    .split(/\s+/)
    .filter(t => t.length > 1 && !STOPWORDS.has(t))
    .map(t => [t, stem(t)]);
  return terms.length ? terms : [[q]];
}

function haystack(r) {
  return `${r.slug.replace(/-/g, " ")} ${r.slug} ${r.description} ${r.category}`.toLowerCase();
}

function matchesTerms(r, terms) {
  const text = haystack(r);
  return terms.every(forms => forms.some(f => text.includes(f)));
}

function render() {
  const q = searchInput.value.trim().toLowerCase();

  searchClear.classList.toggle("visible", q.length > 0);

  const terms = q ? queryTerms(q) : [];
  const filtered = roles.filter(r => {
    const matchesQuery = !terms.length || matchesTerms(r, terms);
    const matchesCat = !activeCategory || r.category === activeCategory;
    return matchesQuery && matchesCat;
  });

  resultCount.textContent = `${filtered.length} of ${roles.length} roles`;

  const visible = filtered.slice(0, shownCount);
  const noResultsMessage = q
    ? `No roles match "${escapeHtml(q)}".`
    : "No roles in this category.";
  roleList.innerHTML = visible.length
    ? visible.map(cardHtml).join("")
    : `<p class="no-results">${noResultsMessage} <button type="button" id="no-results-clear">Clear filters</button></p>`;

  if (!visible.length) {
    document.getElementById("no-results-clear").addEventListener("click", () => {
      searchInput.value = "";
      searchInput.focus();
      setActiveCategory("");
    });
  }

  const remaining = filtered.length - visible.length;
  loadMoreBtn.hidden = remaining <= 0;
  if (remaining > 0) {
    loadMoreBtn.textContent = `Load more roles (${remaining} left)`;
  }
}

function resetAndRender() {
  shownCount = PAGE_SIZE;
  render();
}

function titleCase(slug) {
  return slug.split("-").map(w => w[0].toUpperCase() + w.slice(1)).join(" ");
}

function escapeHtml(str) {
  const div = document.createElement("div");
  div.textContent = str;
  return div.innerHTML;
}

function setActiveCategory(cat) {
  activeCategory = cat;
  categoryFilter.querySelectorAll(".chip").forEach(chip => {
    chip.classList.toggle("active", chip.dataset.cat === cat);
    chip.setAttribute("aria-pressed", chip.dataset.cat === cat ? "true" : "false");
  });
  resetAndRender();
}

async function init() {
  const res = await fetch("data/roles.json");
  const data = await res.json();
  roles = data.roles;
  roleCountEl.textContent = data.count;

  const categories = [...new Set(roles.map(r => r.category))].sort();
  const allChips = ["", ...categories];

  categoryFilter.innerHTML = allChips.map(c => `
    <button type="button" class="chip${c === "" ? " active" : ""}" data-cat="${escapeHtml(c)}" aria-pressed="${c === "" ? "true" : "false"}">${c === "" ? "All" : escapeHtml(titleCase(c))}</button>
  `).join("");

  categoryFilter.querySelectorAll(".chip").forEach(chip => {
    chip.addEventListener("click", () => setActiveCategory(chip.dataset.cat));
  });

  render();
}

searchInput.addEventListener("input", resetAndRender);
searchClear.addEventListener("click", () => {
  searchInput.value = "";
  searchInput.focus();
  resetAndRender();
});
loadMoreBtn.addEventListener("click", () => {
  shownCount += PAGE_SIZE;
  render();
});

init();
