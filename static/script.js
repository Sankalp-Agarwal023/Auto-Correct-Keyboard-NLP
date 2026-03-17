function checkText() {

    let text = document.getElementById("inputText").value;

    fetch("/correct", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            text: text
        })
    })
    .then(response => response.json())
    .then(data => {

        document.getElementById("outputText").value = data.corrected;

        // random confidence for display
        let confidence = Math.floor(Math.random() * 20) + 80;
        document.getElementById("confidenceValue").innerText = confidence + "%";

    })
    .catch(error => {
        console.log("Error:", error);
    });

}