import numpy as np
import matplotlib.pyplot as plt

def adsr_curve(A, D, S, R, t_hold):
    """
    Genera la curva ADSR ideal por tramos.
    - A: ataque (s)
    - D: decay (s)
    - S: sustain level (0..1)
    - R: release (s)
    - t_hold: tiempo que se mantiene la nota tras acabar el decay (s)
      (o sea, duración del sustain)
    """
    # puntos clave
    t0 = 0.0
    t1 = A
    t2 = A + D
    t3 = t2 + t_hold
    t4 = t3 + R

    t = np.array([t0, t1, t2, t3, t4])
    y = np.array([0.0, 1.0, S,   S,  0.0])
    return t, y

def plot_adsr(title, A, D, S, R, t_hold, fname):
    t, y = adsr_curve(A, D, S, R, t_hold)

    plt.figure(figsize=(10, 4))
    plt.plot(t, y, marker="o")
    plt.grid(True)
    plt.title(title)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")

    # leyenda tipo ejemplo
    plt.legend([f"A={A}s, D={D}s, S={S}, R={R}s"], loc="upper right")

    # Etiquetas A D S R (centradas en cada tramo)
    # Attack: 0 -> A
    plt.text(A/2, 0.9, "A", ha="center", va="center")
    # Decay: A -> A+D
    plt.text(A + D/2, (1+S)/2, "D", ha="center", va="center")
    # Sustain: A+D -> A+D+t_hold
    if t_hold > 0:
        plt.text(A + D + t_hold/2, S + 0.05, "S", ha="center", va="center")
    # Release: final
    plt.text(A + D + t_hold + R/2, S/2, "R", ha="center", va="center")

    plt.ylim(-0.05, 1.1)
    plt.tight_layout()
    plt.savefig(fname, dpi=200)
    plt.close()

def main():
    # 1) Genérico (se ve todo claro)
    plot_adsr(
        "Genérico",
        A=0.5, D=0.3, S=0.6, R=0.5, t_hold=0.5,
        fname="work/adsr/generico_ideal.png"
    )

    # 2) Percusivo 1: ataque rápido, sin sustain, decay largo, mantiene hasta extinguir
    # Aquí hacemos t_hold=0 y R pequeño o incluso 0 (porque realmente cae por decay).
    plot_adsr(
        "Percusivo 1",
        A=0.01, D=1.2, S=0.0, R=0.0, t_hold=0.0,
        fname="work/adsr/percusivo1_ideal.png"
    )

    # 3) Percusivo 2: suelta antes => release corto (caída abrupta)
    # Simulamos que suelta después de un rato: t_hold pequeño (o 0) y R corto.
    plot_adsr(
        "Percusivo 2",
        A=0.01, D=1.2, S=0.0, R=0.08, t_hold=0.0,
        fname="work/adsr/percusivo2_ideal.png"
    )

    # 4) Plano: ataque relativamente rápido hasta sustain, sin sobrepasar, release rápido
    plot_adsr(
        "Plano",
        A=0.10, D=0.00, S=1.0, R=0.10, t_hold=2.3,
        fname="work/adsr/plano_ideal.png"
    )

    print("OK: Imágenes generadas en work/adsr/")

if __name__ == "__main__":
    main()
