const roleList = document.getElementById("role-list");
const searchInput = document.getElementById("search");
const categoryFilter = document.getElementById("category-filter");
const resultCount = document.getElementById("result-count");
const roleCountEl = document.getElementById("role-count");

let roles = [];

function render() {
  const q = searchInput.value.trim().toLowerCase();
  const cat = categoryFilter.value;

  const filtered = roles.filter(r => {
    const matchesQuery = !q ||
      r.slug.toLowerCase().includes(q) ||
      r.description.toLowerCase().includes(q) ||
      r.category.toLowerCase().includes(q);
    const matchesCat = !cat || r.category === cat;
    return matchesQuery && matchesCat;
  });

  resultCount.textContent = `${filtered.length} of ${roles.length} roles`;

  roleList.innerHTML = filtered.map(r => `
    <a class="role-card" href="roles/${r.slug}/">
      <h3>${escapeHtml(titleCase(r.slug))}</h3>
      <div class="badges">
        <span class="badge">${escapeHtml(r.category)}</span>
        <span class="badge status-${r.status}">${escapeHtml(r.status)}</span>
        <span class="badge maturity-${r.maturity}">${escapeHtml(r.maturity)}</span>
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

async function init() {
  const res = await fetch("data/roles.json");
  const data = await res.json();
  roles = data.roles;
  roleCountEl.textContent = data.count;

  const categories = [...new Set(roles.map(r => r.category))].sort();
  categoryFilter.innerHTML += categories
    .map(c => `<option value="${escapeHtml(c)}">${escapeHtml(titleCase(c))}</option>`)
    .join("");

  render();
}

searchInput.addEventListener("input", render);
categoryFilter.addEventListener("change", render);

init();
