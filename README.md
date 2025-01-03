# 🧠 AI Code Generator 🖥️

A **Go-based automation tool** that dynamically generates programming code snippets across various languages with the help of AI. 🚀 While the generated code might range from useful to outright nonsensical, this tool provides a fun way to explore AI-assisted code generation. 🤔 It also automates Git commits and pushes to streamline your workflow. 

---

## 🌟 Features

- 🎲 **Random Language Selection**: Generates code snippets in Go, Rust, Python, or JavaScript.  
- ✨ **Dynamic File Management**: Saves each snippet in a well-structured file with proper extensions.  
- 🤖 **AI Integration**: Uses AI models to attempt creating meaningful code (results may vary).  
- 🔄 **Automated Git Workflow**: Adds, commits, and pushes changes to your GitHub repository.  

---

## 🚀 How It Works

1. 🏰 The program navigates to the project directory.
2. 🧑‍💻 Runs `go run` to execute the main program.
3. 📂 Generates a code snippet in the chosen language and saves it in the `AiCode` folder.
4. 📝 Commits the new file with a meaningful message and pushes it to the repository.  

---

## ⚙️ Requirements

- 📦 **Go** installed on your system.  
- 🌐 Access to GitHub with proper permissions.  
- 💡 An AI model accessible from your system (like `ollama`).  

---

## 🛠️ Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AiCodeGen.git
   ```
2. Navigate to the project directory and ensure dependencies are installed.
3. Add the repository path to your Git config for seamless automation.

---

## 🌟 Example Output

- **Generated File**: `AiGenCode123.js`  
- **Snippet Content**:
  ```javascript
  // Example AI-generated JavaScript code
  function add(a, b) {
      return a + b;
  }
  console.log(add(2, 3));
  ```

---

## 🤝 Contributions

Feel free to fork the repository, submit pull requests, or create issues! Let’s make this tool even more awesome. 🎉

--- 

## 📜 License

This project is open-source and licensed under the MIT License.
