(function () {
  const CALL_NUMBERS = {
    "ux-design": "700",
    "system-design": "000",
    "engineering": "620",
    "documentation": "020",
    "automation": "650",
  };

  const catalogEl = document.getElementById("catalog");
  const searchInput = document.getElementById("searchInput");
  const typeButtons = document.querySelectorAll(".type-btn");
  const countSkillsEl = document.getElementById("countSkills");
  const countConnectorsEl = document.getElementById("countConnectors");
  const overlay = document.getElementById("detailOverlay");
  const detailContent = document.getElementById("detailContent");
  const detailClose = document.getElementById("detailClose");

  let activeType = "all";
  let query = "";

  const allItems = [
    ...SKILLS.map((s) => ({ ...s, type: "skill" })),
    ...CONNECTORS.map((c) => ({ ...c, type: "connector" })),
  ];

  countSkillsEl.textContent = SKILLS.length;
  countConnectorsEl.textContent = CONNECTORS.length;

  function matches(item) {
    if (activeType !== "all" && item.type !== activeType) return false;
    if (!query) return true;
    const haystack = `${item.name} ${item.desc} ${item.source || ""} ${item.transport || ""}`.toLowerCase();
    return haystack.includes(query);
  }

  function render() {
    catalogEl.innerHTML = "";
    let visibleTotal = 0;

    CATEGORIES.forEach((cat, idx) => {
      const items = allItems.filter((i) => i.cat === cat.key && matches(i));
      if (items.length === 0) return;
      visibleTotal += items.length;

      const section = document.createElement("section");
      section.className = "section-block";
      section.id = `section-${cat.key}`;

      const head = document.createElement("div");
      head.className = "section-head";
      head.innerHTML = `
        <span class="section-callnum">${CALL_NUMBERS[cat.key]}</span>
        <h2 class="section-title">${cat.label}</h2>
        <span class="section-count">${items.length} ${items.length === 1 ? "entry" : "entries"}</span>
        <span class="section-blurb">${cat.blurb}</span>
      `;
      section.appendChild(head);

      const grid = document.createElement("div");
      grid.className = "card-grid";

      items
        .slice()
        .sort((a, b) => a.name.localeCompare(b.name))
        .forEach((item) => {
          const card = document.createElement("article");
          card.className = "card";
          card.tabIndex = 0;
          card.innerHTML = `
            <div class="card-top">
              <span class="card-name">${item.name}</span>
              <span class="card-tag ${item.type}">${item.type === "skill" ? "Skill" : "Connector"}</span>
            </div>
            <p class="card-desc">${item.desc}</p>
            <div class="card-source">${item.type === "skill" ? item.source : item.transport}</div>
          `;
          card.addEventListener("click", () => openDetail(item, cat));
          card.addEventListener("keypress", (e) => {
            if (e.key === "Enter") openDetail(item, cat);
          });
          grid.appendChild(card);
        });

      section.appendChild(grid);
      catalogEl.appendChild(section);
    });

    if (visibleTotal === 0) {
      const empty = document.createElement("div");
      empty.className = "empty-state";
      empty.textContent = "No entries match that search. Try a different term, or clear the drawer.";
      catalogEl.appendChild(empty);
    }
  }

  function openDetail(item, cat) {
    detailContent.innerHTML = `
      <div class="detail-callnum">${CALL_NUMBERS[cat.key]} · ${cat.label.toUpperCase()} · ${item.type.toUpperCase()}</div>
      <h3 class="detail-name">${item.name}</h3>
      <p class="detail-desc">${item.desc}</p>
      <div class="detail-meta">
        ${item.type === "skill" ? `<div><strong>Source:</strong> ${item.source}</div>` : `<div><strong>Transport:</strong> ${item.transport}</div>`}
      </div>
      <a class="detail-link" href="${item.link}" target="_blank" rel="noopener">View source →</a>
    `;
    overlay.classList.add("open");
  }

  function closeDetail() {
    overlay.classList.remove("open");
  }

  detailClose.addEventListener("click", closeDetail);
  overlay.addEventListener("click", (e) => {
    if (e.target === overlay) closeDetail();
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeDetail();
  });

  searchInput.addEventListener("input", (e) => {
    query = e.target.value.trim().toLowerCase();
    render();
  });

  typeButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      typeButtons.forEach((b) => {
        b.classList.remove("active");
        b.setAttribute("aria-selected", "false");
      });
      btn.classList.add("active");
      btn.setAttribute("aria-selected", "true");
      activeType = btn.dataset.type;
      render();
    });
  });

  render();
})();
