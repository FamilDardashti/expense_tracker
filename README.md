python main.py <command> [--argument value] [--argument value] ...



python main.py add --date 2025-07-01 --amount 120 --category food --description "grocery shopping"
python main.py add --date 2025-07-02 --amount 35.5 --category transport --description "bus ticket"
python main.py add --date 2025-07-02 --amount 18 --category internet --description "mobile data"
python main.py add --date 2025-07-03 --amount 200 --category shopping --description "clothes"
python main.py add --date 2025-07-03 --amount 50 --category health --description "pharmacy"
python main.py add --date 2025-07-04 --amount 65.5 --category education --description "online course"
python main.py add --date 2025-07-04 --amount 30 --category food --description "lunch out"
python main.py add --date 2025-07-05 --amount 12 --category transport --description "subway"
python main.py add --date 2025-07-05 --amount 45 --category entertainment --description "movie ticket"
python main.py add --date 2025-07-06 --amount 25.75 --category food --description "snack + drink"
python main.py add --date 2025-07-06 --amount 100 --category shopping --description "books"
python main.py add --date 2025-07-07 --amount 9.99 --category internet --description "VPN"
python main.py add --date 2025-07-07 --amount 200 --category health --description "doctor visit"
python main.py add --date 2025-07-08 --amount 80 --category education --description "exam fee"
python main.py add --date 2025-07-08 --amount 22 --category food --description "breakfast"
python main.py add --date 2025-07-09 --amount 150 --category shopping --description "tech accessory"
python main.py add --date 2025-07-10 --amount 60 --category food --description "restaurant dinner"
python main.py add --date 2025-07-10 --amount 17 --category transport --description "taxi"
python main.py add --date 2025-07-11 --amount 10 --category donation --description "charity"
python main.py add --date 2025-07-11 --amount 40 --category entertainment --description "concert ticket"


python main.py summary
python main.py history
python main.py history --last5
python main.py history --filtered_by date --date_range_from 2025-07-01 --to 2025-07-15
python main.py history --filtered_by category --category food
python main.py visualize


