#!/bin/bash

# Get the previous month and the year it was in
PREV_MONTH=$(date -v-1m +%m)
PREV_YEAR=$(date -v-1m +%Y)

# Get the month before the previous month and the year it was in
MONTH_BEFORE_PREV=$(date -v-2m +%m)
YEAR_OF_MONTH_BEFORE_PREV=$(date -v-2m +%Y)

# Define start and end dates for the previous month
START_DATE_PREV="$PREV_YEAR-$PREV_MONTH-01"
END_DATE_PREV=$(date -v-1d -v+1m -jf "%Y-%m-%d" "$START_DATE_PREV" +%Y-%m-%d)

# Define start and end dates for the month before the previous month
START_DATE_BEFORE_PREV="$YEAR_OF_MONTH_BEFORE_PREV-$MONTH_BEFORE_PREV-01"
END_DATE_BEFORE_PREV=$(date -v-1d -v+1m -jf "%Y-%m-%d" "$START_DATE_BEFORE_PREV" +%Y-%m-%d)

# Function to fetch and save costs
fetch_and_save() {
    local start_date=$1
    local end_date=$2
    local output_file=$3

    local result=$(aws ce get-cost-and-usage \
        --time-period Start=$start_date,End=$end_date \
        --granularity MONTHLY \
        --metrics "BlendedCost" \
        --group-by Type=DIMENSION,Key=SERVICE \
        --output json)

    echo "$result" | jq -r '.ResultsByTime[0].Groups[] | .Keys[0] + " $" + .Metrics.BlendedCost.Amount' > $output_file
}

# Fetch and save costs for the previous month
fetch_and_save $START_DATE_PREV $END_DATE_PREV "costs_prev_month.txt"

# Fetch and save costs for the month before the previous month
fetch_and_save $START_DATE_BEFORE_PREV $END_DATE_BEFORE_PREV "costs_month_before_prev.txt"

echo "Output saved to costs_prev_month.txt and costs_month_before_prev.txt"
