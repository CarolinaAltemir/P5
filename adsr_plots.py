import matplotlib.pyplot as plt

def plot_adsr(title, A, D, S, R, t_hold):
    t = [0,
         A,
         A + D,
         A + D + t_hold,
         A + D + t_hold + R]

    y = [0,
         1,
         S,
         S,
         0]

    plt.figure(figsize=(8,4))
    plt.plot(t, y, marker='o')
    plt.grid(True)
    plt.title(title)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.legend([f"A={A}s, D={D}s, S={S}, R={R}s"], loc="upper right")
    plt.ylim(-0.05, 1.1)
    plt.show()


# 1) Genérico
plot_adsr(
    "Genérico",
    A=0.15,
    D=0.15,
    S=0.6,
    R=0.15,
    t_hold=0.25
)

# 2) Percusivo 1
plot_adsr(
    "Percusivo 1",
    A=0.01,
    D=0.60,
    S=0.0,
    R=0.15,
    t_hold=0.0
)

# 3) Percusivo 2
plot_adsr(
    "Percusivo 2",
    A=0.01,
    D=0.60,
    S=0.0,
    R=0.05,
    t_hold=0.0
)

# 4) Plano
plot_adsr(
    "Plano (violín)",
    A=0.10,
    D=0.00,
    S=1.0,
    R=0.10,
    t_hold=0.70
)
