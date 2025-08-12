function aiSearch() {
    var user_query = document.getElementById('displayText').value;
    if (user_query=="") {
        console.log("Empty Query");
        return;
    }
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    const raw = JSON.stringify({
        "query": user_query
    });

    const requestOptions = {
        method: "POST",
        headers: myHeaders,
        body: raw,
        redirect: "follow"
    };

    fetch("http://localhost:8000/search", requestOptions)
        .then((response) => response.text())
        .then((result) => {
            console.log(result);
            const result_json = JSON.parse(result);
            const urls = JSON.parse(result_json.recommended_urls);
            console.log(urls);
            console.log(typeof urls);
            // Find a target container in the DOM
            const container = document.getElementById("results");
            container.innerHTML = ""; // Clear previous results

            // Loop over URLs and create <a> tags
            urls.forEach(url => {
                const link = document.createElement("a");
                link.href = url;          // set URL
                link.textContent = url;   // display URL text
                container.appendChild(link);
                container.appendChild(document.createElement("br")); // line break
            });
        })
        .catch((error) => console.error(error));
}