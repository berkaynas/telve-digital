document.addEventListener("DOMContentLoaded", () => {
    const releasesGrid = document.querySelector(".releases-grid");

    fetch("/static/data/releases.json")
        .then(response => response.json())
        .then(data => {
            data.forEach(release => {
                const card = document.createElement("div");
                card.className = "release-card";

                // Eğer 'type' varsa tireyi ekle, yoksa sadece 'title' göster
                const releaseInfo = release.type 
                    ? `<span>${release.title}</span> - <span>${release.type}</span>` 
                    : `<span>${release.title}</span>`;

                card.innerHTML = `
                    <img src="${release.image}" alt="${release.title}">
                    <div class="release-info">
                        ${releaseInfo}
                    </div>
                    <div class="overlay">
                        ${release.spotify ? `
                        <div class="social-links">
                            <a href="${release.spotify}" target="_blank"><i class="bi bi-spotify"></i></a>
                        </div>
                        ` : ""}
                    </div>
                `;
                releasesGrid.appendChild(card);
            });
        })
        .catch(error => console.error("Error loading releases:", error));
});
