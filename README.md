# Guida: Setup ambiente Python + OpenCV su Linux

## 1. Verifica se Python è già installato
```bash
python3 --version
```
Se restituisce un numero di versione (es. `Python 3.12.3`), Python è già presente. Su Ubuntu 24.04 Python 3 è preinstallato di default, quindi in genere questo passo è già a posto.

Se il comando non viene riconosciuto, installa Python:
```bash
sudo apt update
sudo apt install python3 -y
```

## 2. Installa pip e il modulo venv
```bash
sudo apt update
sudo apt install python3-pip python3-venv -y
```
Verifica che pip sia installato:
```bash
pip3 --version
```

## 3. Crea la cartella del progetto
```bash
mkdir -p ~/Documenti/DAFN/Masocco/es_opencv
cd ~/Documenti/DAFN/Masocco/es_opencv
```
(Adatta il percorso alla tua struttura di cartelle.)

## 4. Crea l'ambiente virtuale
```bash
python3 -m venv venv
```
Questo crea una cartella `venv/` contenente una copia isolata di Python e pip, separata da quella di sistema.

## 5. Attiva l'ambiente virtuale
```bash
source venv/bin/activate
```
Il prompt del terminale mostrerà `(venv)` all'inizio della riga: è la conferma che l'ambiente è attivo.

## 6. Aggiorna pip dentro l'ambiente (buona pratica)
```bash
pip install --upgrade pip
```

## 7. Installa OpenCV (con moduli contrib) e numpy
```bash
pip install opencv-contrib-python numpy
```

**Pesi indicativi:**

| Pacchetto | Download | Spazio su disco |
|---|---|---|
| `opencv-contrib-python` | ~80-90 MB | ~280-300 MB |
| `numpy` | ~15-18 MB | ~60 MB |
| **Totale** | **~100 MB** | **~350 MB** |

> ⚠️ **Importante: installa UN SOLO pacchetto OpenCV.**
> Esistono tre varianti che occupano lo stesso namespace `cv2` e **non vanno mai installate insieme**: `opencv-python`, `opencv-python-headless`, `opencv-contrib-python`. Se ne installi più di una contemporaneamente (es. perché una libreria terza come `ultralytics` ne installa una come dipendenza mentre tu ne avevi già un'altra), il modulo `cv2` risultante può risultare incompleto o corrotto, causando errori come:
> ```
> AttributeError: module 'cv2' has no attribute 'CascadeClassifier'
> ```
> anche se il codice è corretto. Se succede, verifica quante ne hai installate:
> ```bash
> pip list | grep -i opencv
> ```
> Se ne trovi più di una, disinstallale tutte e reinstalla solo `opencv-contrib-python` (è la più completa, include anche i moduli extra):
> ```bash
> pip uninstall opencv-python opencv-python-headless opencv-contrib-python -y
> pip install opencv-contrib-python
> ```

## 8. Verifica l'installazione
```bash
python3 -c "import cv2; import numpy as np; print('OpenCV version:', cv2.__version__); print('Numpy version:', np.__version__)"
```
Se stampa entrambe le versioni senza errori, l'ambiente è pronto.

## 9. Salva le dipendenze (per riprodurre l'ambiente in futuro)
```bash
pip freeze > requirements.txt
```
Per ricreare l'ambiente da questo file in futuro (es. su un altro PC):
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 10. Apri il progetto in VS Code
```bash
code .
```
Poi seleziona l'interprete corretto:
1. `Ctrl+Shift+P` → digita `Python: Select Interpreter`
2. Scegli quello che contiene `./venv/bin/python`

Se apri un terminale integrato in VS Code, dovrebbe attivare automaticamente il venv (vedrai `(venv)` nel prompt). Se non succede, attivalo manualmente con il comando del punto 11.

---

## 11. (Opzionale) Installare PyTorch + Ultralytics (YOLO) per il deep learning

Se vuoi passare dall'object detection classica (template matching, Haar Cascade) a modelli di deep learning come YOLO, ti serve PyTorch come motore di calcolo sottostante.

### 11.1 Installa PyTorch in versione CPU-only

Se il tuo laptop **non ha una GPU NVIDIA dedicata** (come nella maggior parte dei laptop consumer), conviene installare la build CPU-only di PyTorch: è più leggera perché non include i binari CUDA, che sarebbero inutili senza GPU compatibile.

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

> ⚠️ **Installa `torch` e `torchvision` insieme, nello stesso comando.**
> Se li installi separatamente (prima `torch`, poi `ultralytics` che tira dentro `torchvision` da un altro indice), rischi di ottenere versioni di `torch` e `torchvision` non compatibili tra loro, causando un errore tipo:
> ```
> RuntimeError: operator torchvision::nms does not exist
> ```
> che si verifica al primo utilizzo del modello (non all'importazione). La soluzione è disinstallare entrambi e reinstallarli **insieme** dallo stesso indice:
> ```bash
> pip uninstall torch torchvision -y
> pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
> ```

**Peso indicativo:** ~190-200 MB per `torch` CPU-only, più qualche decina di MB per `torchvision`.

### 11.2 Installa Ultralytics

```bash
pip install ultralytics
```

Questo comando, se `torch`/`torchvision` sono già installati e compatibili, non li reinstalla — aggiunge solo `ultralytics` e le sue dipendenze minori (numpy, pillow, pyyaml, matplotlib, ecc., alcune probabilmente già presenti).

### 11.3 Verifica l'installazione

```bash
python -c "import ultralytics; ultralytics.checks()"
```

Questo stampa versione di Python, versione di PyTorch, sistema operativo e conferma se è disponibile una GPU CUDA (su CPU-only risulterà assente, ed è normale).

### 11.4 Primo utilizzo di un modello YOLO

Al primo `YOLO('yolov8n.pt')` nel codice, Ultralytics scarica automaticamente i pesi del modello pre-addestrato (per `yolov8n.pt`, circa 6 MB) da GitHub e li salva nella cartella corrente. I download successivi useranno il file già presente, senza riscaricarlo.

---

## Come attivare l'ambiente virtuale
Ogni volta che vuoi lavorare al progetto, apri un terminale e digita:
```bash
cd ~/Documenti/DAFN/Masocco/es_opencv
source venv/bin/activate
```

## Come disattivare l'ambiente virtuale
```bash
deactivate
```
Questo riporta il terminale a usare il Python di sistema, senza disinstallare nulla.

---

## Come disinstallare tutto (rimuovere l'ambiente e le librerie)
Con l'ambiente disattivato, basta cancellare la cartella `venv`:
```bash
deactivate
rm -rf venv
```
Questo rimuove completamente Python isolato, pip, OpenCV, numpy, PyTorch/Ultralytics (se installati) e tutto ciò che è stato installato nell'ambiente. Il codice sorgente (es. `test.py`) e il resto del progetto restano intatti, se tenuti fuori dalla cartella `venv`.

Per ricreare l'ambiente in seguito, ripeti i punti 4-7 (e opzionalmente l'11, se serve YOLO) — oppure usa `requirements.txt` come mostrato al punto 9.
