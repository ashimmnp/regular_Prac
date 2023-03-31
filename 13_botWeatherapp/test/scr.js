const form = document.querySelector('#locationForm');
const weatherInfo = document.querySelector('#weatherInfo');
const locationInput = "london"; // Set the location to London

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  try {
    const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${locationInput}&appid={YOUR_API_KEY}`);
    const weatherData = await response.json();
    
    const temp = weatherData.main.temp;
    const humidity = weatherData.main.humidity;
    const windSpeed = weatherData.wind.speed;
    const weatherDescription = weatherData.weather[0].description;
    
    const weatherInfoHTML = `
      <p>Temperature: ${temp} K</p>
      <p>Humidity: ${humidity} %</p>
      <p>Wind Speed: ${windSpeed} m/s</p>
      <p>Weather Description: ${weatherDescription}</p>
    `;
    
    weatherInfo.innerHTML = weatherInfoHTML;
  } catch (error) {
    console.error(error);
  }
});
