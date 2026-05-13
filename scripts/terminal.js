document.addEventListener('DOMContentLoaded', () => {
    const terminalOutput = document.getElementById('terminal-output');
    const terminalInput = document.getElementById('terminal-input');

    if (!terminalOutput || !terminalInput) return;

    const commands = {
        help: "Available commands: <br> - <b>whoami</b>: Who am I? <br> - <b>skills</b>: View my tech stack <br> - <b>projects</b>: Quick links to my best work <br> - <b>clear</b>: Clear the terminal <br> - <b>contact</b>: Get my email",
        whoami: "Pranjal Kumar Shukla<br>Backend & Machine Learning Developer.<br>I specialize in Spring Boot microservices, Docker, Kubernetes, and Computer Vision.",
        skills: "<b>Backend</b>: Spring Boot, Microservices, Hibernate<br><b>Languages</b>: Python, Java, C++, JavaScript<br><b>DevOps</b>: Docker, Kubernetes, GitHub Actions, AWS<br><b>ML</b>: Scikit-learn, OpenCV, TensorFlow, Pandas",
        projects: "<b>1. AgriProject</b>: Spring Boot + ML Microservices<br><b>2. K8s Orchestration</b>: Full-stack Kubernetes monitoring<br><b>3. Ascraa AI</b>: OpenCV matching platform<br>Type 'clear' to clean the screen.",
        contact: "Email: <a href='mailto:pranjalmss2005@gmail.com' style='color:var(--accent-1); text-decoration:underline;'>pranjalmss2005@gmail.com</a><br>LinkedIn: <a href='https://www.linkedin.com/in/shukla-pranjal/' target='_blank' style='color:var(--accent-1); text-decoration:underline;'>shukla-pranjal</a>",
        sudo: "Nice try! This incident will be reported. Just kidding.",
        clear: "CLEAR"
    };

    function printOutput(text, isCommand = false) {
        const line = document.createElement('div');
        line.className = isCommand ? 'terminal-command-line' : 'terminal-response-line';
        
        if (isCommand) {
            line.innerHTML = `<span class="prompt">guest@portfolio:~$</span> ${text}`;
        } else {
            line.innerHTML = text;
        }
        
        terminalOutput.appendChild(line);
        terminalOutput.scrollTop = terminalOutput.scrollHeight;
    }

    terminalInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
            const val = this.value.trim().toLowerCase();
            if (val) {
                printOutput(val, true);
                
                if (val === 'clear') {
                    terminalOutput.innerHTML = '';
                } else if (commands[val]) {
                    printOutput(commands[val]);
                } else {
                    printOutput(`bash: ${val}: command not found. Type 'help' for a list of commands.`);
                }
            }
            this.value = '';
        }
    });

    // Focus terminal input when clicking anywhere on the terminal window
    document.querySelector('.terminal-window').addEventListener('click', () => {
        terminalInput.focus();
    });
});
