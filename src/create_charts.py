import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Dữ liệu thực tế
experiments = ['Baseline\n(0.01, 0.3, 1.2)', 
               'Ngưỡng cao\n(0.02, 0.5, 2.0)', 
               'Ngưỡng thấp\n(0.005, 0.2, 1.0)']
num_rules = [1794, 73, 2445]
lift_avg = [13.57, 11.01, 11.41]
conf_avg = [54, 62, 46]

# Biểu đồ 1: So sánh số lượng luật
plt.figure(figsize=(10, 6))
colors = ['#3498db', '#e74c3c', '#f39c12']
bars = plt.bar(experiments, num_rules, color=colors, edgecolor='black', linewidth=1.5)

plt.title('Ảnh hưởng của ngưỡng tham số đến số lượng luật', 
          fontsize=16, weight='bold', pad=20)
plt.ylabel('Số lượng luật kết hợp', fontsize=13)
plt.xlabel('Thí nghiệm (Support, Confidence, Lift)', fontsize=13)

# Thêm giá trị trên cột
for bar, val in zip(bars, num_rules):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 50,
             f'{val:,}', ha='center', va='bottom', 
             fontsize=12, weight='bold')

plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('chart1_num_rules.png', dpi=300, bbox_inches='tight')
print("✅ Đã lưu: chart1_num_rules.png")
plt.show()

# Biểu đồ 2: So sánh chất lượng (Lift và Confidence)
fig, ax1 = plt.subplots(figsize=(10, 6))

x = np.arange(len(experiments))
width = 0.35

# Lift bars
bars1 = ax1.bar(x - width/2, lift_avg, width, 
                label='Lift trung bình', color='#3498db', 
                edgecolor='black', linewidth=1.5)
ax1.set_ylabel('Lift trung bình', fontsize=13, weight='bold')
ax1.set_xlabel('Thí nghiệm', fontsize=13)
ax1.set_xticks(x)
ax1.set_xticklabels(['Baseline', 'Cao', 'Thấp'], fontsize=12)
ax1.tick_params(axis='y', labelcolor='#3498db')
ax1.set_ylim(0, max(lift_avg) * 1.2)

# Confidence bars
ax2 = ax1.twinx()
bars2 = ax2.bar(x + width/2, conf_avg, width, 
                label='Confidence TB (%)', color='#e74c3c',
                edgecolor='black', linewidth=1.5)
ax2.set_ylabel('Confidence trung bình (%)', fontsize=13, weight='bold')
ax2.tick_params(axis='y', labelcolor='#e74c3c')
ax2.set_ylim(0, max(conf_avg) * 1.3)

# Thêm giá trị
for bar, val in zip(bars1, lift_avg):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 0.3,
             f'{val:.2f}', ha='center', va='bottom', 
             fontsize=10, weight='bold', color='#3498db')

for bar, val in zip(bars2, conf_avg):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + 1,
             f'{val}%', ha='center', va='bottom', 
             fontsize=10, weight='bold', color='#e74c3c')

plt.title('So sánh chất lượng luật: Lift vs Confidence', 
          fontsize=16, weight='bold', pad=20)

# Legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, 
           loc='upper left', fontsize=11)

plt.tight_layout()
plt.savefig('chart2_quality_comparison.png', dpi=300, bbox_inches='tight')
print("✅ Đã lưu: chart2_quality_comparison.png")
plt.show()

print("\n📊 Tóm tắt kết quả:")
print("="*50)
for i, exp in enumerate(['Baseline', 'Ngưỡng cao', 'Ngưỡng thấp']):
    print(f"{exp:15} | Luật: {num_rules[i]:5} | Lift: {lift_avg[i]:5.2f} | Conf: {conf_avg[i]:3}%")
