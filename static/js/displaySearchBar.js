const textArray = [
    "Why is my bill so high?",
    "Will there an outage tommorow?",
    "How do I request a new connection?",
    "When are prices in my area lowest?",
    "Are my bills pending?"
];
let currentIndex = 0;

const displayElement = document.getElementById("displayText");
function updateText() {
    // Only update if the field is empty (no user input)
    if (displayElement.value === "") {
        setTimeout(() => {
            displayElement.placeholder = textArray[currentIndex];
            currentIndex = (currentIndex + 1) % textArray.length;
            console.log("Placeholder updated:", displayElement.placeholder);
        }, 100);
    }
}

// Start cycling through placeholder text every 3 seconds
updateText();
setInterval(updateText, 3000);
