async function uploadFile() {

    const fileInput = document.getElementById("fileInput");
    const loading = document.getElementById("loading");
    const result = document.getElementById("result");
    const downloadBtn = document.getElementById("downloadBtn");

    const file = fileInput.files[0];

    if (!file) {
        alert("Please select a file first.");
        return;
    }

    loading.innerText = "AI is analyzing your code...";
    result.innerHTML = "";
    downloadBtn.style.display = "none";

    const formData = new FormData();
    formData.append("file", file);

    try {

        const response = await fetch("http://127.0.0.1:8000/upload", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        console.log("Backend response:", data);

        loading.innerText = "Documentation Generated Successfully";

        // Render Markdown nicely
        result.innerHTML = marked.parse(data.ai_analysis);

        downloadBtn.style.display = "block";

    } catch (error) {

        console.error("Upload error:", error);

        loading.innerText = "Error generating documentation.";

    }
}



async function analyzeRepo() {

    const repoUrl = document.getElementById("repoUrl").value;
    const loading = document.getElementById("loading");
    const result = document.getElementById("result");
    const downloadBtn = document.getElementById("downloadBtn");

    if (!repoUrl) {
        alert("Please enter a GitHub repository URL.");
        return;
    }

    loading.innerText = "Analyzing GitHub repository...";
    result.innerHTML = "";
    downloadBtn.style.display = "none";

    try {

        const response = await fetch("http://127.0.0.1:8000/analyze-repo", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(repoUrl)

        });

        const data = await response.json();

        console.log("Repo analysis:", data);

        loading.innerText = "Repository Documentation Generated";

        result.innerHTML = marked.parse(data.documentation);

        downloadBtn.style.display = "block";

    } catch (error) {

        console.error("Repo analysis error:", error);

        loading.innerText = "Error analyzing repository.";

    }
}