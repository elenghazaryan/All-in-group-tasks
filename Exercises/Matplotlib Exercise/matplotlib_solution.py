import matplotlib.pyplot as plt
import pandas as pd

PATH = "C:\\Users\\User\\Desktop\\allin_tasks\\Matplotlib Exercise\\company_sales_data.csv"


def question1():
    df = pd.read_csv(PATH)

    profit_list = df['total_profit'].tolist()
    month_list = df['month_number'].tolist()
    plt.plot(month_list, profit_list, label='Month-wise Profit data of last year')
    plt.xlabel('Month number')
    plt.ylabel('Profit in dollar')
    plt.xticks(month_list)
    plt.title('Company profit per month')
    plt.yticks([100000, 200000, 300000, 400000, 500000])
    plt.show()


def question2():
    df = pd.read_csv(PATH)
    profit_list = df['total_profit'].tolist()
    month_list = df['month_number'].tolist()

    plt.plot(month_list, profit_list, label='Profit data of last year',
             color='r', marker='o', markerfacecolor='k',
             linestyle='--', linewidth=3)

    plt.xlabel('Month Number')
    plt.ylabel('Profit in dollar')
    plt.legend(loc='lower right')
    plt.title('Company Sales data of last year')
    plt.xticks(month_list)
    plt.yticks([100000, 200000, 300000, 400000, 500000])
    plt.show()


def question3():
    df = pd.read_csv(PATH)
    month_list = df['month_number'].tolist()
    face_cream_sales_data = df['facecream'].tolist()
    face_wash_sales_data = df['facewash'].tolist()
    tooth_paste_sales_data = df['toothpaste'].tolist()
    bathing_soap_sales_data = df['bathingsoap'].tolist()
    shampoo_sales_data = df['shampoo'].tolist()
    moisturizer_sales_data = df['moisturizer'].tolist()

    plt.plot(month_list, face_cream_sales_data, label='Face crem Sales Data', marker='o', linewidth=3)
    plt.plot(month_list, face_wash_sales_data, label='Face Wash Sales Data', marker='o', linewidth=3)
    plt.plot(month_list, tooth_paste_sales_data, label='ToothPaste Sales Data', marker='o', linewidth=3)
    plt.plot(month_list, bathing_soap_sales_data, label='bathing soap sales data', marker='o', linewidth=3)
    plt.plot(month_list, shampoo_sales_data, label='Shampoo sales data', marker='o', linewidth=3)
    plt.plot(month_list, moisturizer_sales_data, label='moisturizer sales data', marker='o', linewidth=3)

    plt.xlabel('Month Number')
    plt.ylabel('Sales units in number')
    plt.legend(loc='upper left')
    plt.xticks(month_list)
    plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
    plt.title('Sales data')
    plt.show()


def question4():
    df = pd.read_csv(PATH)
    month_list = df['month_number'].tolist()
    tooth_paste_sales_data = df['toothpaste'].tolist()

    plt.scatter(month_list, tooth_paste_sales_data, label='Tooth paste Sales data')

    plt.xlabel('Month Number')
    plt.ylabel('Number of units Sold')

    plt.legend(loc='upper left')
    plt.title(' Tooth paste Sales data')
    plt.xticks(month_list)
    plt.grid(True, linewidth=1, linestyle="--")
    plt.show()


def question5():
    df = pd.read_csv(PATH)
    month_list = df['month_number'].tolist()
    face_cream_sales_data = df['facecream'].tolist()
    face_wash_sales_data = df['facewash'].tolist()

    plt.bar([a - 0.25 for a in month_list], face_cream_sales_data, width=0.25, label='Face Cream sales data', align='edge')
    plt.bar([a + 0.25 for a in month_list], face_wash_sales_data, width=-0.25, label='Face Wash sales data', align='edge')

    plt.xlabel('Month Number')
    plt.ylabel('Sales units in number')
    plt.legend(loc='upper left')
    plt.title(' Sales data')

    plt.xticks(month_list)
    plt.grid(True, linewidth=1, linestyle="--")
    plt.title('Facewash and facecream sales data')
    plt.show()


def question6():
    df = pd.read_csv(PATH)
    month_list = df['month_number'].tolist()
    bathing_soap_sales_data = df['bathingsoap'].tolist()
    plt.bar(month_list, bathing_soap_sales_data)
    plt.xlabel('Month Number')
    plt.ylabel('Sales units in number')
    plt.title(' Sales data')
    plt.xticks(month_list)
    plt.grid(True, linewidth=1, linestyle="--")
    plt.title('bathingsoap sales data')
    plt.savefig('C:\\Users\\User\\Desktop\\allin_tasks\\Matplotlib Exercise\\sales_data_of_bathingsoap.png', dpi=150)
    plt.show()


def question7():
    df = pd.read_csv(PATH)
    profit_list = df['total_profit'].tolist()
    profit_range = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
    plt.hist(profit_list, profit_range, label='Profit data')
    plt.xlabel('profit range in dollar')
    plt.ylabel('Actual Profit in dollar')
    plt.legend(loc='upper left')
    plt.xticks(profit_range)
    plt.title('Profit data')
    plt.show()


def question8():
    df = pd.read_csv(PATH)
    month_list = df['month_number'].tolist()
    labels = ['FaceCream', 'FaseWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']
    sales_data = [df['facecream'].sum(), df['facewash'].sum(), df['toothpaste'].sum(),
                 df['bathingsoap'].sum(), df['shampoo'].sum(), df['moisturizer'].sum()]
    plt.axis("equal")
    plt.pie(sales_data, labels=labels, autopct='%1.1f%%')
    plt.legend(loc='lower right')
    plt.title('Sales data')
    plt.show()


def question9():
    df = pd.read_csv(PATH)
    month_list = df['month_number'].tolist()
    bathing_soap = df['bathingsoap'].tolist()
    face_wash_sales_data = df['facewash'].tolist()

    f, axarr = plt.subplots(2, sharex=True)
    axarr[0].plot(month_list, bathing_soap, label='Bathingsoap Sales Data', color='k', marker='o', linewidth=3)
    axarr[0].set_title('Sales data of  a Bathingsoap')
    axarr[1].plot(month_list, face_wash_sales_data, label='Face Wash Sales Data', color='r', marker='o', linewidth=3)
    axarr[1].set_title('Sales data of  a facewash')

    plt.xticks(month_list)
    plt.xlabel('Month Number')
    plt.ylabel('Sales units in number')
    plt.show()


def question10():
    df = pd.read_csv(PATH)
    month_list = df['month_number'].tolist()
    face_cream_sales_data = df['facecream'].tolist()
    face_wash_sales_data = df['facewash'].tolist()
    tooth_paste_sales_data = df['toothpaste'].tolist()
    bathing_soap_sales_data = df['bathingsoap'].tolist()
    shampoo_sales_data = df['shampoo'].tolist()
    moisturizer_sales_data = df['moisturizer'].tolist()

    plt.plot([], [], color='m', label='face Cream', linewidth=5)
    plt.plot([], [], color='c', label='Face wash', linewidth=5)
    plt.plot([], [], color='r', label='Tooth paste', linewidth=5)
    plt.plot([], [], color='k', label='Bathing soap', linewidth=5)
    plt.plot([], [], color='g', label='Shampoo', linewidth=5)
    plt.plot([], [], color='y', label='Moisturizer', linewidth=5)

    plt.stackplot(month_list, face_cream_sales_data, face_wash_sales_data, tooth_paste_sales_data,
                  bathing_soap_sales_data, shampoo_sales_data, moisturizer_sales_data,
                  colors=['m', 'c', 'r', 'k', 'g', 'y'])

    plt.xlabel('Month Number')
    plt.ylabel('Sales unints in Number')
    plt.title('Alll product sales data using stack plot')
    plt.legend(loc='upper left')
    plt.show()

question10()