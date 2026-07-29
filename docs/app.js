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

function render() {
  const q = searchInput.value.trim().toLowerCase();

  searchClear.classList.toggle("visible", q.length > 0);

  const filtered = roles.filter(r => {
    const matchesQuery = !q ||
      r.slug.toLowerCase().includes(q) ||
      r.description.toLowerCase().includes(q) ||
      r.category.toLowerCase().includes(q);
    const matchesCat = !activeCategory || r.category === activeCategory;
    return matchesQuery && matchesCat;
  });

  resultCount.textContent = `${filtered.length} of ${roles.length} roles`;

  const visible = filtered.slice(0, shownCount);
  roleList.innerHTML = visible.map(cardHtml).join("");

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
