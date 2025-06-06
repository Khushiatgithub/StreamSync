document.getElementById("summaryForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const plot = document.getElementById("movieTitle").value;

  const response = await fetch("http://localhost:5000/summarize", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ plot: plot })
  });

  const data = await response.json();
  document.getElementById("summary").innerText = data.summary;
});
