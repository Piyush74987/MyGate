async function sendChat() {
    const prompt = document.getElementById("chatInput").value;
    const res = await fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({prompt})
    });
    const data = await res.json();
    document.getElementById("chatOutput").innerText = JSON.stringify(data, null, 2);
}
