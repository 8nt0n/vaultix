// load your css file into index.html
function loadStylesheet(url) {
    let link = document.createElement('link'); // Create a link element
    link.rel = 'stylesheet'; // Set the rel attribute to "stylesheet"
    link.href = url;         // Set the href attribute to the URL of the stylesheet
    
    document.head.appendChild(link); // Append the link element to the head
}

// Create and append the HTML Widget to index.html
function createMediaWidget() {
    // Create the main container
    var widget = document.createElement('div');
    widget.id = 'media-widget';

    // Create the header container
    let header = document.createElement('div');
    header.id = 'media-widget-header';

    // Create the header text
    let headerText = document.createElement('p');
    headerText.textContent = 'Streamed';
    headerText.style.fontWeight = '600';
    headerText.style.marginLeft = '15px';
    headerText.style.marginRight = '148px';
    header.appendChild(headerText);

    // Create the minimize button
    let minimizeButton = document.createElement('img');
    minimizeButton.src = '../static/img/MINIMIEREN.png';
    minimizeButton.alt = 'minimize';
    minimizeButton.className = 'minimize';
    minimizeButton.id = 'media-widget-minimize';
    minimizeButton.onclick = function () {
        minimize('media-widget');
    };
    header.appendChild(minimizeButton);

    // Create the close button
    let closeButton = document.createElement('img');
    closeButton.src = '../static/img/SCHLIESSEN.png';
    closeButton.alt = 'Close';
    closeButton.className = 'close';
    closeButton.onclick = function () {
        closeElement('media-widget');
    };
    header.appendChild(closeButton);

    // Append the header to the main container
    widget.appendChild(header);


    Media_Links = ["videos", "games" ,"audios", "files"]

    for (let i = 0; i<4; i++) {
        let Media_image = document.createElement("img") 
        Media_image.src = `../static/img/MediaWidget/Media-${Media_Links[i]}.png`
        Media_image.style = "margin: 11px 0px;"
        
        let Media_anchor = document.createElement("a")
        Media_anchor.style = "display: inline-block; height: 97px;"
        Media_anchor.setAttribute('href', `${Media_Links[i]}`)
        Media_anchor.setAttribute('target', "_blank")
    
        Media_anchor.appendChild(Media_image)
        widget.appendChild(Media_anchor)
    
        // grey divider
        let divider = document.createElement("div")
        divider.style = "height: 1px; width: 335px; margin: 0px; margin-left: 22px; margin-top: -3px; background-color: #CACACA;"
        widget.appendChild(divider)
    }
   
    // Append the widget to the body
    document.body.appendChild(widget);
}

document.addEventListener("DOMContentLoaded", function() {

    __open_media__()
});


function __open_media__() {
    original_height["media-widget"] = "438px"; // Add the height of the widget to height dict. (for minimizing / unfolding the widget)

    loadStylesheet('../static/@apps/media/media.css')

    createMediaWidget()

    dragElement(document.getElementById("media-widget")) //Make widget draggable

    OpenWidgets.push("media")
}
