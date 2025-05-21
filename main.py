import turtle
import time
from analog_watch import AnalogWatch
from digital_watch import DigitalWatch

def main():
 
    def run_analog_clock():
        analog_clock = AnalogWatch(x=0, y=0, radius=150)
        while True:
            analog_clock.update_time()
            time.sleep(1)

    # Пример использования цифровых часов
    def run_digital_clock():
        digital_clock = DigitalWatch(x=0, y=0, is_24_hour_format=True)

        def handle_click(x, y):
            digital_clock.toggle_format()

        digital_clock.screen.onclick(handle_click)

        def update_digital_clock():
            digital_clock.update_time()
            digital_clock.screen.ontimer(update_digital_clock, 1000)

        update_digital_clock()

    # Пример одновременного отображения обоих часов
    def run_both_clocks():
        screen = turtle.Screen()
        screen.setup(width=800, height=400)
        screen.bgcolor("white")
        screen.tracer(0)

        analog_clock = AnalogWatch(x=-200, y=0, radius=150)
        digital_clock = DigitalWatch(x=200, y=0, is_24_hour_format=True)

        def handle_click_digital(x, y):
            if 100 < x < 300 and -50 < y < 50:
                digital_clock.toggle_format()

        screen.onclick(handle_click_digital)

        def update_all_clocks():
            analog_clock.update_time()
            digital_clock.update_time()
            screen.update()
            screen.ontimer(update_all_clocks, 1000)

        update_all_clocks()

    
    run_both_clocks()

    turtle.done()

if __name__ == "__main__":
    main() 