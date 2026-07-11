const roleList = document.getElementById("role-list");
const searchInput = document.getElementById("search");
const searchClear = document.getElementById("search-clear");
const categoryFilter = document.getElementById("category-filter");
const resultCount = document.getElementById("result-count");
const roleCountEl = document.getElementById("role-count");

let roles = [];
let activeCategory = "";

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

  roleList.innerHTML = filtered.map(r => `
    <a class="role-card" href="roles/${r.slug}/">
      <h3>${escapeHtml(titleCase(r.slug))}</h3>
      <div class="badges">
        <span class="badge">${escapeHtml(r.category)}</span>
        <span class="badge status-${r.status}">${escapeHtml(r.status)}</span>
      </div>
      <p>${escapeHtml(r.description)}</p>
    </a>
  `).join("");
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
  render();
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

searchInput.addEventListener("input", render);
searchClear.addEventListener("click", () => {
  searchInput.value = "";
  searchInput.focus();
  render();
});

init();
