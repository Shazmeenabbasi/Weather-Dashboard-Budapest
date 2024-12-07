// Fetch weather data from the backend
fetch('http://localhost:5000/weather')
    .then(response => response.json())
    .then(data => {
        const container = document.getElementById('weather-container');
        if (data && data.weather) {
            container.innerHTML = `
                <h2>${data.name}</h2>
                <p>${data.weather[0].description}</p>
                <p>Temperature: ${data.main.temp}°C</p>
                <p>Humidity: ${data.main.humidity}%</p>
            `;
        } else {
            container.innerHTML = '<p>Unable to fetch weather data.</p>';
        }
    })
    .catch(error => {
        console.error('Error fetching weather data:', error);
        document.getElementById('weather-container').innerHTML = '<p>Error loading weather data.</p>';
    });
