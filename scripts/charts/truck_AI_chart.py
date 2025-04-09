import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from scripts.AI_scripts.truck_order_ai import Truck_Prediction

def generate_combined_chart():
    results, mse = Truck_Prediction.run_prediction()  
    
    ids = []
    ai_lava = []
    ai_hot_fudge = []
    ai_blizzard = []
    ai_chocolate = []
    ai_vanilla = []

    for x in results:
        ids.append(x[0])
        ai_lava.append(x[2])
        ai_hot_fudge.append(x[4])
        ai_blizzard.append(x[6])
        ai_chocolate.append(x[8])
        ai_vanilla.append(x[10])

    plt.plot(ids, ai_lava, label='AI lava', marker='o')
    plt.plot(ids, ai_hot_fudge, label='AI hot_fudge', marker='o')
    plt.plot(ids, ai_blizzard, label='AI blizzard', marker='o')
    plt.plot(ids, ai_chocolate, label='AI chocolate', marker='o')
    plt.plot(ids, ai_vanilla, label='AI vanilla', marker='o')

    # Add labels, title, and legend
    plt.xlabel('ID')
    plt.ylabel('Totals')
    plt.title('AI Truck Order')
    plt.legend()
    plt.grid()

    # Save the figure
    plt.savefig('static/charts/truck_ai_chart.png')
    plt.close()