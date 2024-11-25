const apiKey = "a8eae53f4871eeb106ee9759e803008a";
const apiURL = "https://api.openweathermap.org/data/2.5/weather?units=metric&q=";

const searchButton = document.querySelector(".search button");
const searchBox = document.querySelector(".search input");
const cityName = searchBox.value;
const image = document.querySelector(".weather-icon")

async function checkWeather(city) {
    const respone = await fetch(apiURL + city + `&appid=${apiKey}`);
    var data = await respone.json();

    console.log(data);

    document.querySelector(".city").innerHTML = data.name;
    document.querySelector(".temp").innerHTML = data.main.temp + "°C";
    document.querySelector(".humidity").innerHTML = data.main.humidity + "%";
    document.querySelector(".wind").innerHTML = data.wind.speed + "km/h";


    switch (data.weather[0].main) {
        case 'Clear':
            image.src = 'img/clear.png';
            break;

        case 'Cloud':
            image.src = 'img/clouds.png';
            break;

        case 'Drizzle':
            image.src = 'img/drizzle.png';
            break;

        case 'Humidity':
            image.src = 'img/humidity.png';
            break;

        case 'Mist':
            image.src = 'img/mist.png';
            break;

        case 'Rain':
            image.src = 'img/rain.png';
            break;

        case 'Snow':
            image.src = 'img/snow.png';
            break;

        case 'Wind':
            image.src = 'img/wind.png';
            break;
    }
}


searchButton.addEventListener("click", () => {
    checkWeather(searchBox.value);
})























/*searchButton.addEventListener("click", () =>{
    if(cityName === '') {
        return;
    }

    fetch(apiURL)
        .then(respone => respone.json())
        .then(json =>{
            console.log(json);
            switch (json.weather[0].main) {
                case 'Clear':
                    image.src = 'img/clear.png';
                    break;

                case 'Cloud':
                    image.src = 'img/clouds.png';
                    break;

                case 'Drizzle':
                    image.src = 'img/drizzle.png';
                    break;

                case 'Humidity':
                    image.src = 'img/humidity.png';
                    break;

                case 'Mist':
                    image.src = 'img/mist.png';
                    break;

                case 'Rain':
                    image.src = 'img/rain.png';
                    break;

                case 'Snow':
                    image.src = 'img/snow.png';
                    break;

                case 'Wind':
                    image.src = 'img/wind.png';
                    break;
            }
        })
    
})

*/
