package main

import (
	"fmt"
	"log"
	"math/rand"
	"os"
	"os/exec"
	"strconv"
	"strings"
  "regexp"
)

var languages = map[string]string{
	"go":       "go",
	"rust":     "rs",
	"javascript": "js",
	"python":   "py",
}

func getCounter(filename string) int {
	data, err := os.ReadFile(filename)
	if err != nil {
		if os.IsNotExist(err) {
			return 1 // Start from 1 if file doesn't exist
		}
		log.Fatalf("Error reading counter file: %v", err)
	}

	counter, err := strconv.Atoi(strings.TrimSpace(string(data)))
	if err != nil {
		log.Fatalf("Error parsing counter file: %v", err)
	}

	return counter
}

func updateCounter(filename string, counter int) {
	err := os.WriteFile(filename, []byte(fmt.Sprintf("%d", counter)), 0644)
	if err != nil {
		log.Fatalf("Error updating counter file: %v", err)
	}
}


func cleanCodeFile(fileName, language string) {
	data, err := os.ReadFile(fileName)
	if err != nil {
		log.Fatalf("Error reading file: %v", err)
	}

	re := regexp.MustCompile(fmt.Sprintf("(?s)```%s\\s(.*?)```", language))
	matches := re.FindStringSubmatch(string(data))

	if len(matches) < 2 {
		log.Fatalf("No valid code block found in file: %s", fileName)
	}

	cleanedCode := matches[1]
	err = os.WriteFile(fileName, []byte(cleanedCode), 0644)
	if err != nil {
		log.Fatalf("Error writing cleaned code to file: %v", err)
	}
}
func main() {

	languagesKeys := make([]string, 0, len(languages))
	for lang := range languages {
		languagesKeys = append(languagesKeys, lang)
	}
	selectedLang := languagesKeys[rand.Intn(len(languagesKeys))]
	extension := languages[selectedLang]

	counterFile := "counter.txt"
	counter := getCounter(counterFile)

	fileName := fmt.Sprintf("/home/majdif47/CoDevHub/projects/go/AiCodeGen/AiGenCode%d.%s", counter, extension)

	cmd := exec.Command("ollama", "run", "llama3.2", fmt.Sprintf("write some code that does something useful thats is not something simple like a random password generator in %s only give me the code", selectedLang))
	output, err := cmd.Output()
	if err != nil {
		log.Fatalf("Error running ollama command: %v", err)
	}
	err = os.WriteFile(fileName, output, 0644)
	if err != nil {
		log.Fatalf("Error writing output to file: %v", err)
	}
  cleanCodeFile(fileName, selectedLang)
	updateCounter(counterFile, counter+1)
  gitCommands := [][]string{
	  {"git", "add", "."},
	  {"git", "commit", "-m", fmt.Sprintf("Add %s", fileName)},
	  {"git", "push"},
  }

for _, args := range gitCommands {
	cmd := exec.Command(args[0], args[1:]...) // First element is the command, the rest are arguments
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	err := cmd.Run()
	if err != nil {
		log.Fatalf("Error running git command (%v): %v", args, err)
	}
}

	fmt.Printf("Generated code saved to %s and pushed to GitHub.\n", fileName)
}

