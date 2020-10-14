{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)\n",
    "\n",
    "* Your task is to create a Python script that analyzes the records to calculate each of the following:\n",
    "\n",
    "  * The total number of months included in the dataset\n",
    "\n",
    "  * The net total amount of \"Profit/Losses\" over the entire period\n",
    "\n",
    "  * The average of the changes in \"Profit/Losses\" over the entire period\n",
    "\n",
    "  * The greatest increase in profits (date and amount) over the entire period\n",
    "\n",
    "  * The greatest decrease in losses (date and amount) over the entire period\n",
    "\n",
    "* As an example, your analysis should look similar to the one below:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"PyBank Homework Solution.\"\"\"\n",
    "# Dependencies\n",
    "import csv\n",
    "import os\n",
    "# Files to load and output (Remember to change these)\n",
    "file_to_load = os.path.join(\"Resources\", \"budget_data.csv\")\n",
    "file_to_output = os.path.join(\"analysis\", \"budget_analysis.txt\")\n",
    "# Track various financial parameters\n",
    "total_months = 0\n",
    "month_of_change = []\n",
    "net_change_list = []\n",
    "greatest_increase = [\"\", 0]\n",
    "greatest_decrease = [\"\", 9999999999999999999]\n",
    "total_net = 0\n",
    "# Read the csv and convert it into a list of dictionaries\n",
    "with open(file_to_load) as financial_data:\n",
    "    reader = csv.reader(financial_data)\n",
    "    # Read the header row\n",
    "    header = next(reader)\n",
    "    # Extract first row to avoid appending to net_change_list\n",
    "    first_row = next(reader)\n",
    "    total_months += 1\n",
    "    total_net += int(first_row[1])\n",
    "    prev_net = int(first_row[1])\n",
    "    for row in reader:\n",
    "        # Track the total\n",
    "        total_months += 1\n",
    "        total_net += int(row[1])\n",
    "        # Track the net change\n",
    "        net_change = int(row[1]) - prev_net\n",
    "        prev_net = int(row[1])\n",
    "        net_change_list += [net_change]\n",
    "        month_of_change += [row[0]]\n",
    "        # Calculate the greatest increase\n",
    "        if net_change > greatest_increase[1]:\n",
    "            greatest_increase[0] = row[0]\n",
    "            greatest_increase[1] = net_change\n",
    "        # Calculate the greatest decrease\n",
    "        if net_change < greatest_decrease[1]:\n",
    "            greatest_decrease[0] = row[0]\n",
    "            greatest_decrease[1] = net_change\n",
    "# Calculate the Average Net Change\n",
    "net_monthly_avg = sum(net_change_list) / len(net_change_list)\n",
    "# Generate Output Summary\n",
    "output = (\n",
    "    f\"Financial Analysis\\n\"\n",
    "    f\"----------------------------\\n\"\n",
    "    f\"Total Months: {total_months}\\n\"\n",
    "    f\"Total: ${total_net}\\n\"\n",
    "    f\"Average  Change: ${net_monthly_avg:.2f}\\n\"\n",
    "    f\"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\\n\"\n",
    "    f\"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\\n\")\n",
    "# Print the output (to terminal)\n",
    "print(output)\n",
    "# Export the results to text file\n",
    "with open(file_to_output, \"w\") as txt_file:\n",
    "    txt_file.write(output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
