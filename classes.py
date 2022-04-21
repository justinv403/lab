class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Initialization of the TV object
        """
        self.__channel: int = Television.MIN_CHANNEL
        self.__volume: int = Television.MIN_VOLUME
        self.__status: bool = False

    def power(self) -> None:
        """
        Toggles the power state of the TV object
        """
        
        if self.__status:
            self.__status = False
        else:
            self.__status = True


    def channel_up(self) -> None:
        """
        Increases the channel of the TV, and goes back to the minimum channel if it is already at its max
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            elif self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decreases the channel of the TV, and goes to the max if the channel is already at the minimum value
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            elif self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Increases the volume by 1 as long as the max has not already been reached
        """
        
        if self.__status:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreases the volume by 1 as long as the min has not already been reached
        """
        if self.__status:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        This method returns the TV status using the format shown in the comments of main.py

        :return: TV status using the format shown in the comments of main.py
        """
        return "TV status: Is on = " + str(self.__status) +", Channel = " + str(self.__channel) + ", Volume = " + str(self.__volume)