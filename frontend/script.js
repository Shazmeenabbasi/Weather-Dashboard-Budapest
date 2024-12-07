document.addEventListener("DOMContentLoaded", () => {
    fetch("http://localhost:8080/weather")
        .then((response) => response.json())
        .then((data) => {
            const weatherDiv = document.getElementById("weather");
            if (data.error) {
                weatherDiv.innerHTML = `<p>Error: ${data.error}</p>`;
            } else {
                weatherDiv.innerHTML = `
                    <p>City: ${data.city}</p>
                    <p>Temperature: ${data.temperature}°C</p>
                    <p>Description: ${data.description}</p>
                `;
            }
        })
        .catch((error) => {
            document.getElementById("weather").innerHTML = `<p>Error fetching data: ${error.message}</p>`;
        });
});
