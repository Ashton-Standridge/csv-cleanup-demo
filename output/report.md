# Data cleanup report

| Metric | Count |
|---|---|
| input rows | 44 |
| blank rows | 1 |
| names changed | 43 |
| emails fixed | 33 |
| emails invalid | 0 |
| phones normalized | 31 |
| phones missing | 8 |
| dates normalized | 29 |
| dates missing | 10 |
| duplicates removed | 3 |
| output rows | 40 |

## Before / after (first 10 rows)

| Before | After |
|---|---|
| DeShawn nguyen  / deshawn.nguyen0 @ example.com / n/a / 1/1/2024 | Deshawn Nguyen / deshawn.nguyen0@example.com /  / 2024-01-01 |
| MARIA GARCIA /  maria.garcia1@example.com  / 4785550001 / 2/2/2025 | Maria Garcia / maria.garcia1@example.com / (478) 555-0001 / 2025-02-02 |
| o'brien smith / obrien.smith2@example.com / 1-478-555-0002 / June 3, 2024 | O'Brien Smith / obrien.smith2@example.com / (478) 555-0002 / 2024-06-03 |
| MARIA o'neil / maria.o'neil3@example.com / 4785550003 / January 4, 2025 | Maria O'Neil / maria.o'neil3@example.com / (478) 555-0003 / 2025-01-04 |
| john GARCIA / JOHN.GARCIA4@EXAMPLE.COM / n/a /  | John Garcia / john.garcia4@example.com /  /  |
| john macleod / john.macleod5@example.com / 478.555.0005 / 6/6/2025 | John MacLeod / john.macleod5@example.com / (478) 555-0005 / 2025-06-06 |
|   li  van der berg / li.vanderberg6 @ example.com / 478.555.0006 /  | Li van der Berg / li.vanderberg6@example.com / (478) 555-0006 /  |
| MARIA van der berg / maria.vanderberg7@example,com / n/a / 2025-08-08 | Maria van der Berg / maria.vanderberg7@example.com /  / 2025-08-08 |
| MARIA o'neil /  maria.o'neil8@example.com  / (478) 555-0008 /  | Maria O'Neil / maria.o'neil8@example.com / (478) 555-0008 /  |
| MARIA smith / maria.smith9@example,com / 478.555.0009 / January 10, 2025 | Maria Smith / maria.smith9@example.com / (478) 555-0009 / 2025-01-10 |
