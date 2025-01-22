// load your css file into index.html
function loadStylesheet(url) {
    let link = document.createElement('link'); // Create a link element
    link.rel = 'stylesheet'; // Set the rel attribute to "stylesheet"
    link.href = url;         // Set the href attribute to the URL of the stylesheet
    
    document.head.appendChild(link); // Append the link element to the head
}


// Create and append the HTML Widget to index.html
function createCalenderWidget() {
    // Create the main container
    let widget = document.createElement('div');
    widget.id = 'calender-widget';

    // Create the header container
    let header = document.createElement('div');
    header.id = 'calender-widget-header';

    // Create the header text
    let headerText = document.createElement('p');
    headerText.textContent = 'Calender';
    headerText.style.fontWeight = '600';
    headerText.style.marginLeft = '15px';
    header.appendChild(headerText);

    // Create the minimize button
    let minimizeButton = document.createElement('img');
    minimizeButton.src = '../static/img/MINIMIEREN.png';
    minimizeButton.alt = 'minimize';
    minimizeButton.className = 'minimize';
    minimizeButton.id = 'calender-widget-minimize';
    minimizeButton.onclick = function () {
        minimize('calender-widget');
    };
    header.appendChild(minimizeButton);

    // Create the close button
    let closeButton = document.createElement('img');
    closeButton.src = '../static/img/SCHLIESSEN.png';
    closeButton.alt = 'Close';
    closeButton.className = 'close';
    closeButton.onclick = function () {
        closeElement('calender-widget');
    };
    header.appendChild(closeButton);

    // Append the header to the main container
    widget.appendChild(header);

    // Create the date container
    let dateContainer = document.createElement('div');
    dateContainer.id = 'calender-widget-dateContainer';
    widget.appendChild(dateContainer);

    // Create the day and month container
    let dayMonthContainer = document.createElement('div');
    dayMonthContainer.id = 'calender-widget-dayMonthContainer';
    widget.appendChild(dayMonthContainer);

    // Append the widget to the body
    document.body.appendChild(widget);
}






// lookup how many days are in a month (eg. January: 31)
function getDaysInMonth(month, year) {
    return new Date(year, month, 0).getDate();
}






// gets the current month (wow i know such awesome commentary)
function get_current_month() { 
    let month = ["January","February","March","April","May","June","July","August","September","October","November","December"];

    let d = new Date();
    return month[d.getMonth()];
}





// Create every date in the month (center)
function WidgetCreateDays() {
    
    // Lookup, how many days are in the current month
    let calenderDays = getDaysInMonth(new Date().getMonth() + 1, new Date().getFullYear());
    let CalenderDateContainer = document.getElementById("calender-widget-dateContainer")

    // For each day in the month, append it to the calender widget as a paragraph
    for (let i=1; i <= calenderDays; i++){
        let c_day = document.createElement("p");
        c_day.textContent = i;

        c_day.setAttribute("class","c_day"); 

        //Highlight CURRENT date with red background box
        if (new Date().getDate() === i) {
            c_day.setAttribute("class","c_day_highlight"); 
        }

        CalenderDateContainer.appendChild(c_day);
        
    }
}




// Create the small grey date (bottom right)
function WidgetCreateSmallDate() {
    let dayMonthContainer = document.getElementById("calender-widget-dayMonthContainer")
    let c_day_month = document.createElement("p");

    c_day_month.textContent = `${get_current_month()} ${new Date().getDate()}`;
    c_day_month.setAttribute("class","c_day_month");

    dayMonthContainer.appendChild(c_day_month)
}





// main function of the script
document.addEventListener("DOMContentLoaded", function() {
  
    __open_calender__()

});



// required | How should your widget respond when its opened?
function __open_calender__() {

    original_height["calender-widget"] = "225px"; // Add the height of the widget to height dict. (for minimizing / unfolding the widget)

    loadStylesheet('../static/@apps/calender/calender.css') // load calender specific stylesheet

    createCalenderWidget() // Spawn the DOM elements

    dragElement(document.getElementById("calender-widget")) //Make widget draggable

    WidgetCreateDays() // add all the days (center of the calender)

    WidgetCreateSmallDate()  // the small grey text (bottom right)


    OpenWidgets.push("calender") // add the calender to the list of open widgets
}