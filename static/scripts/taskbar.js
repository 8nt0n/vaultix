var TaskbarDynamicApps = { 
    "taskbar-icon-0" : "calender-widget", // Document ID of the image : App to open when its clicked
    "taskbar-icon-1" : "media-widget", 
    "taskbar-icon-2" : "docs-widget",
    "taskbar-icon-3" : "plantera-widget",
    "taskbar-icon-4" : "AppStore-widget"
};


function InitDynamicIcons() {
    let DynamicIcon = [];

    for (let i = 0; i < 5; i++) {
        DynamicIcon[i] = document.getElementById(`taskbar-icon-${i}`);
        console.log(TaskbarDynamicApps[i])
        DynamicIcon[i].setAttribute("onclick", `openApp('${TaskbarDynamicApps['taskbar-icon-'+i]}')`)
        console.log(DynamicIcon)
    }
}



document.addEventListener("DOMContentLoaded", function() {
    InitDynamicIcons() //document.get each Icon in the Taskbar
});
