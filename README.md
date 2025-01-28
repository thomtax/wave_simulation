# Wave Simulation Framework

## Introduzione

`wave_simulation` è un framework modulare in Python per simulare l'equazione d'onda di D'Alembert in 1D e 2D. Utilizza il metodo delle differenze finite per calcolare l'evoluzione temporale delle onde e offre strumenti di visualizzazione animata per analizzare i risultati.

## Struttura del Progetto

```
wave_simulation/
├── wave_simulation/
│   ├── __init__.py
│   ├── parameters.py
│   ├── stability.py
│   ├── initialization.py
│   ├── solver.py
│   ├── boundary_conditions.py
│   └── visualization.py
├── examples/
│   ├── simulate_1d_fixed.py
│   ├── simulate_1d_free.py
│   ├── simulate_2d_membrane.py
│   └── simulate_2d_surface.py
├── tests/
│   ├── test_stability.py
│   ├── test_initialization.py
│   └── test_solver.py
├── requirements.txt
└── README.md
```

- **`wave_simulation/`**: Pacchetto principale contenente tutti i moduli.
- **`examples/`**: Script di esempio che mostrano come utilizzare il framework per varie simulazioni.
- **`tests/`**: Suite di test unitari per garantire il corretto funzionamento dei moduli.
- **`requirements.txt`**: Elenco delle dipendenze necessarie.
- **`README.md`**: Documentazione e istruzioni di utilizzo.

## Installazione

### 1. **Prerequisiti**

Assicurati di avere Python 3.6 o superiore installato sul tuo sistema.

### 2. **Clonare il Repository**

```bash
git clone https://github.com/thomtax/wave_simulation.git
cd wave_simulation
```

### 3. **Creare un Ambiente Virtuale (Opzionale ma Consigliato)**

```bash
python -m venv venv
source venv/bin/activate  # Su Windows: venv\Scripts\activate
```

### 4. **Installare le Dipendenze**

```bash
pip install -r requirements.txt
```

## Utilizzo

Il pacchetto `wave_simulation` può essere utilizzato direttamente negli script Python o tramite gli script di esempio forniti.

### 1. **Esempi Disponibili**

Nella cartella `examples/` sono presenti diversi script per diverse simulazioni:

- **`simulate_1d_fixed.py`**: Simulazione di un'onda 1D con condizioni al contorno fisse.
- **`simulate_1d_free.py`**: Simulazione di un'onda 1D con condizioni al contorno libere.
- **`simulate_2d_membrane.py`**: Simulazione di una membrana 2D con condizioni al contorno fisse.
- **`simulate_2d_surface.py`**: Simulazione di onde di superficie 2D.

### 2. **Eseguire un'Esempio**

Per eseguire una simulazione 1D con condizioni al contorno fisse:

```bash
python examples/simulate_1d_fixed.py
```

### 3. **Personalizzare i Parametri**

Puoi modificare i parametri delle simulazioni direttamente nei file degli esempi o creare nuovi script utilizzando le classi e le funzioni del pacchetto.

#### **Esempio di Personalizzazione:**

```python
from wave_simulation import Parameters1D, initialize_1d, check_stability_1d, solve_1d_fixed, animate_1d

def main():
    # Definizione dei parametri personalizzati
    params = Parameters1D(
        L=2.0,
        T_total=10.0,
        c=0.3,
        sigma=0.05,
        Nx=300,
        Nt=1000
    )
    x, t, u, dx, dt = initialize_1d(params)
    check_stability_1d(params.c, dt, dx)
    c_coeff = (params.c * dt / dx) ** 2
    u = solve_1d_fixed(u, params, c_coeff)
    animate_1d(x, t, u, title="Simulazione Onda 1D Personalizzata")

if __name__ == "__main__":
    main()
```

## Dettaglio dei Moduli

### **1. `parameters.py`**

Gestisce la definizione e la gestione dei parametri della simulazione.

#### **Classi:**

- **`Parameters1D`**: Parametri per simulazioni 1D.
- **`Parameters2D`**: Parametri per simulazioni 2D.

### **2. `stability.py`**

Contiene funzioni per verificare le condizioni di stabilità delle simulazioni.

#### **Funzioni:**

- **`check_stability_1d(c, dt, dx)`**: Verifica la condizione di stabilità per simulazioni 1D.
- **`check_stability_2d(c, dt, dx, dy)`**: Verifica la condizione di stabilità per simulazioni 2D.

### **3. `initialization.py`**

Gestisce l'inizializzazione dei dati della simulazione, incluse le condizioni iniziali.

#### **Funzioni:**

- **`initialize_1d(params)`**: Inizializza una simulazione 1D con condizioni al contorno fisse.
- **`initialize_1d_free(params)`**: Inizializza una simulazione 1D con condizioni al contorno libere.
- **`initialize_2d(params)`**: Inizializza una simulazione 2D.

### **4. `solver.py`**

Contiene i metodi principali delle differenze finite per evolvere l'equazione d'onda.

#### **Funzioni:**

- **`solve_1d_fixed(u, params, c_coeff)`**: Risolve l'equazione d'onda 1D con condizioni al contorno fisse.
- **`solve_1d_free(u, params, c_coeff)`**: Risolve l'equazione d'onda 1D con condizioni al contorno libere.
- **`solve_2d_fixed(u, params, c_coeff)`**: Risolve l'equazione d'onda 2D con condizioni al contorno fisse.

### **5. `boundary_conditions.py`**

Definisce varie condizioni al contorno per la simulazione.

#### **Funzioni:**

- **`fixed_boundary(u_frame)`**: Applica condizioni al contorno fisse (u=0 agli estremi).
- **`free_boundary(u, n)`**: Applica condizioni al contorno libere (derivata spaziale zero agli estremi).

### **6. `visualization.py`**

Gestisce tutti gli aspetti di visualizzazione, incluse le animazioni.

#### **Funzioni:**

- **`animate_1d(x, t, u, title)`**: Crea un'animazione 3D per simulazioni 1D.
- **`animate_2d_membrane(X, Y, t, u, title)`**: Crea un'animazione 3D per simulazioni di membrane 2D.
- **`animate_2d_surface(t, X, Y, u, title)`**: Crea un'animazione 2D per onde di superficie 2D.

## Testing

Il framework include una suite di test per verificare il corretto funzionamento dei vari moduli.

### **Eseguire i Test**

Per eseguire tutti i test, utilizza il seguente comando nella directory principale del progetto:

```bash
python -m unittest discover -s tests
```

### **Aggiungere Nuovi Test**

Puoi aggiungere nuovi test creando ulteriori file `.py` nella cartella `tests/` e seguendo la struttura esistente.

## Contribuire

I contributi sono benvenuti! Se desideri contribuire al progetto, segui questi passaggi:

1. **Fork del Repository**
2. **Creare un Branch per la Tua Funzionalità (`git checkout -b feature/nuova-funzionalità`)**
3. **Commit delle Modifiche (`git commit -m 'Aggiunge nuova funzionalità')`**
4. **Push del Branch (`git push origin feature/nuova-funzionalità`)**
5. **Aprire una Pull Request**

## Licenza

Questo progetto è concesso in licenza sotto la [MIT License](LICENSE).

## Contact

Per domande o suggerimenti, apri una issue nel repository GitHub o contatta `[thomastax03@gmail.com]`.

## Riferimenti

- Metodo delle Differenze Finite: [Wikipedia](https://it.wikipedia.org/wiki/Metodo_delle_differenze_finestre)
- Documentazione di Matplotlib: [Matplotlib](https://matplotlib.org/stable/contents.html)
- Documentazione di NumPy: [NumPy](https://numpy.org/doc/stable/)