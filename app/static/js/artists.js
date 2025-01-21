document.addEventListener('DOMContentLoaded', async () => {
    try {
        const artistsGrid = document.querySelector('.artists-grid');

        // JSON dosyasından verileri çek
        const response = await fetch('/static/data/artists.json');
        if (!response.ok) {
            throw new Error('Sanatçı verileri yüklenemedi.');
        }

        const artists = await response.json();

        artists.forEach(artist => {
            const { Name, Social, ImagePath } = artist;

            const imageUrl = ImagePath || '/static/artist_images/default_artist.jpg';
            const instagramLink = Social?.instagram
                ? `<a href="${Social.instagram}" target="_blank"><i class="bi bi-instagram"></i></a>`
                : '';
            const spotifyLink = Social?.spotify
                ? `<a href="${Social.spotify}" target="_blank"><i class="bi bi-spotify"></i></a>`
                : '';

            const artistCard = `
                <div class="artist-card">
                    <img src="${imageUrl}" alt="${Name}">
                    <div class="artist-name">${Name}</div>
                    <div class="overlay">
                        <div class="social-links">
                            ${instagramLink}
                            ${spotifyLink}
                        </div>
                    </div>
                </div>
            `;

            artistsGrid.innerHTML += artistCard;
        });
    } catch (error) {
        console.error('Sanatçı verileri yüklenemedi:', error);
    }
});
