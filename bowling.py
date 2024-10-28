from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        self._frame = []
        pass
    
    def add_frame(self, frame: Frame) -> None:
        self._frame.append(frame)
        pass

    def get_frame_at(self, i: int) -> Frame:
        return self._frame[i]
        pass

    def calculate_score(self) -> int:
        score = 0
        is_spare = False
        for frame in self._frames:
            if is_spare:
                score = score + frame.get_first_throw() + frame.get_second_throw();
                is_spare = False;
            if frame.is_spare():
                is_spare = True;
        pass

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        pass

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
