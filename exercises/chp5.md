class SayDays:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        self.month_days = [31, 29 if self.is_leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def days(self):
        return sum(self.month_days[:self.month - 1]) + self.day

    def days_left(self):
        total_year_days = 366 if self.is_leap else 365
        return total_year_days - self.days()

    def weekday(self):
        y, m, d = self.year, self.month, self.day
        if m < 3:
            m += 12
            y -= 1
        K = y % 100
        J = y // 100
        h = (d + (13 * (m + 1)) // 5 + K + K // 4 + J // 4 - 2 * J) % 7
        return h

    def weekday_name(self):
        names = ["토요일", "일요일", "월요일", "화요일", "수요일", "목요일", "금요일"]
        return names[self.weekday()]

while True:
    user_input = input("날짜(년 월 일) 입력 (종료: q): ")
    if user_input.lower() == 'q':
        break
    
    try:
        y, m, d = map(int, user_input.split())
        sd = SayDays(y, m, d)
        
        print(f"경과 일수: {sd.days()}일")
        print(f"남은 일수: {sd.days_left()}일")
        print(f"요일 숫자: {sd.weekday()}")
        print(f"요일 이름: {sd.weekday_name()}")
        print("-" * 20)
    except ValueError:
        print("다시 입력하세요.")

<img width="361" height="76" alt="image" src="https://github.com/user-attachments/assets/5cd8d73a-893e-4a96-aa6d-364fea14d245" />
