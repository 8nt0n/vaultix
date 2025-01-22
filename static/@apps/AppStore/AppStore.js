let AppStorePage = "Cool"

// load your css file into index.html
function loadStylesheet(url) {
    let link = document.createElement('link'); // Create a link element
    link.rel = 'stylesheet'; // Set the rel attribute to "stylesheet"
    link.href = url;         // Set the href attribute to the URL of the stylesheet
    
    document.head.appendChild(link); // Append the link element to the head
}


// Create and append the HTML Widget to index.html
function createAppStoreWidget() {
    // Create the main container
    let widget = document.createElement('div');
    widget.id = 'AppStore-widget';

    // Create the header container
    let header = document.createElement('div');
    header.id = 'AppStore-widget-header';

    // Create the header text
    let headerText = document.createElement('p');
    headerText.textContent = 'App Store';
    headerText.style.fontWeight = '600';
    headerText.style.marginLeft = '15px';
    headerText.style.marginRight = '487px';
    header.appendChild(headerText);

    // Create the minimize button
    let minimizeButton = document.createElement('img');
    minimizeButton.src = '../static/img/MINIMIEREN.png';
    minimizeButton.alt = 'minimize';
    minimizeButton.className = 'minimize';
    minimizeButton.id = 'AppStore-widget-minimize';
    minimizeButton.onclick = function () {
        minimize('AppStore-widget');
    };
    header.appendChild(minimizeButton);

    // Create the close button
    let closeButton = document.createElement('img');
    closeButton.src = '../static/img/SCHLIESSEN.png';
    closeButton.alt = 'Close';
    closeButton.className = 'close';
    closeButton.onclick = function () {
        closeElement('AppStore-widget');
    };
    header.appendChild(closeButton);

    // Append the header to the main container
    widget.appendChild(header);

    // Append the widget to the body
    document.body.appendChild(widget);
}


function createAppStoreSideBar() {
    let widget = document.getElementById("AppStore-widget")

    let Sidebar = document.createElement("div")
    Sidebar.setAttribute("class", "sideBar")

    let Categories = ["Cool", "Games", "Tools", "Media"]

    for (let i = 0; i < Categories.length; i++) {
        let Categorie = document.createElement("img")
        Categorie.setAttribute("src", `../static/@apps/AppStore/${Categories[i]}.png`)
        Categorie.setAttribute("onclick", `AppStorePage = '${Categories[i]}'; updateCategoriePath(); loadAppStoreApps(AppStore${Categories[i]})`)
        Sidebar.appendChild(Categorie)
    }

    widget.appendChild(Sidebar) 
}


function createAppStoreSearchBar() {
    let widget = document.getElementById("AppStore-widget")

    let Searchbar = document.createElement("div")
    Searchbar.setAttribute("class", "searchBar")
    Searchbar.setAttribute("id", "AppStore-widget-SearchBar")

    widget.appendChild(Searchbar)

    let Searchinput = document.createElement("Input")
    Searchinput.setAttribute("class", "SearchInput")
    Searchinput.setAttribute("placeholder", "Search")

    Searchbar.appendChild(Searchinput)


    let StoreIcon = document.createElement("img")
    StoreIcon.setAttribute("src", "../static/@apps/AppStore/Icon.png")
    StoreIcon.setAttribute("class", "StoreIcon")
    Searchbar.appendChild(StoreIcon)


    let AppStorePath = document.createElement("p")
    AppStorePath.innerHTML = "AppStore/"
    AppStorePath.style = "font-size: 16px; font-weight: 600; position: absolute; top: 16px; left: 246px;"
    Searchbar.appendChild(AppStorePath)

}

function createAppStoreContainer() {
    let widget = document.getElementById("AppStore-widget")

    StoreContainer = document.createElement("div")
    StoreContainer.setAttribute("id", "AppStore-AppsContainer")
    StoreContainer.setAttribute("class", "StoreContainer")

    widget.appendChild(StoreContainer)
}

function loadAppStoreApps(ARRAY) {

    const div = document.getElementById('AppStore-AppsContainer');
    div.replaceChildren();

    for (let i = 0; i < ARRAY.length; i++) {

        let StoreContainer = document.getElementById("AppStore-AppsContainer")
    
        let AppWidget = document.createElement("div")
        AppWidget.setAttribute("class", "AppWidget")
        StoreContainer.appendChild(AppWidget)


        let AppWidgetIcon = document.createElement("img")
        AppWidgetIcon.setAttribute("src", `https://raw.githubusercontent.com/8nt0n/VaultixStore/main/${ARRAY[i]}/meta/StoreIcon.png`)
        AppWidgetIcon.setAttribute("class", "AppWidgetIcon")
        AppWidget.appendChild(AppWidgetIcon)

        let AppWidgetHeader = document.createElement("p")
        AppWidgetHeader.innerHTML = ARRAY[i]
        AppWidgetHeader.setAttribute("class", "AppWidgetHeader")
        AppWidget.appendChild(AppWidgetHeader)

        let AppWidgetDescription = document.createElement("p")

        let URL = `https://raw.githubusercontent.com/8nt0n/VaultixStore/refs/heads/main/${ARRAY[i]}/meta/Info.txt`

        fetch(URL)
            .then(response => {
                if (!response.ok) {
                    AppWidgetDescription.innerHTML = "error fetching description"
                }
                return response.text();
            })
            .then(data => {
                if (data.length < 36) {
                    AppWidgetDescription.innerHTML = data;
                }
                else if (data.length > 35) {
                    AppWidgetDescription.innerHTML = data.substring(0, 35) + "...";
                }
            })

        AppWidgetDescription.setAttribute("class", "AppWidgetDescription")
        AppWidget.appendChild(AppWidgetDescription)



        let AppWidgetInstall = document.createElement("img")
        AppWidgetInstall.setAttribute("src", "../static/@apps/AppStore/Install.png")
        AppWidgetInstall.setAttribute("class", "AppWidgetInstall")
        AppWidgetInstall.setAttribute("AppId", `${ARRAY[i]}`)
        AppWidget.appendChild(AppWidgetInstall)


        let AppWidgetGithub = document.createElement("img")
        AppWidgetGithub.setAttribute("src", "../static/@apps/AppStore/Github.png")
        AppWidgetGithub.setAttribute("class", "AppWidgetGithub")
        AppWidgetGithub.setAttribute("onclick", `window.open('https://github.com/8nt0n/VaultixStore/tree/main/${ARRAY[i]}', '_blank');`)
        AppWidget.appendChild(AppWidgetGithub)
    }

    MakeInstallButtonWork() // Bro listen i dont know how to name it but it does what it says...
}

function updateCategoriePath() {
    let Searchbar = document.getElementById("AppStore-widget-SearchBar")

    let CurrentPath = document.createElement("img")
    CurrentPath.setAttribute("src", `../static/@apps/AppStore/${AppStorePage}.png`)
    CurrentPath.setAttribute("class", "AppStoreCurrentPath")
    Searchbar.appendChild(CurrentPath)
}

function MakeInstallButtonWork() {
    const images = document.querySelectorAll('.AppWidgetInstall');
            
    images.forEach(image => {
        image.addEventListener('click', () => {
            const AppId = image.getAttribute('AppId');
            
            // Make a POST request to the Flask server
            fetch('/AppStoreAppInstall', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ AppId : AppId })  // Changed to match Flask key
            })
            .then(response => response.json())
            .then(data => {
                console.log(data.message); // Handle response
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });
}



// required | How should your widget respond when its opened?
function __open_AppStore__() {

    loadStylesheet('../static/@apps/AppStore/AppStore.css') // load calender specific stylesheet

    createAppStoreWidget() // Spawn the DOM elements

    createAppStoreSideBar()

    createAppStoreSearchBar()

    createAppStoreContainer()

    loadAppStoreApps(AppStoreCool)

    dragElement(document.getElementById("AppStore-widget")) //Make widget draggable

    updateCategoriePath()


    original_height["AppStore-widget"] = "467px"; // Add the height of the widget to height dict. (for minimizing / unfolding the widget
    OpenWidgets.push("AppStore") // add the calender to the list of open widgets

}

