from src.Player import Player
class Game():
    
    def __init__(self, player1:Player,player2:Player):
        self.player1=player1
        self.player2=player2
    
    def get_score(self)->str:
        points_player1=self.player1.get_points()
        print (points_player1)
        points_player2=self.player2.get_points()
        if points_player1==points_player2:
            if points_player1==0:
                return "Love-All"
            if points_player1==1:
                return "Fifteen-All"
            if points_player1==2:
                return "Thirty-All"
            return "Deuce"
        if points_player1>points_player2:
            if points_player1>=4:
                if points_player1-points_player2>1:
                    return "Win for player1"
                return "Advantage player1"
            else:
                if points_player1==1:
                    return "Fifteen-Love"
                if points_player1==2:
                    if points_player2==0:
                        return "Thirty-Love"
                    return "Thirty-Fifteen"
                if points_player2==0:
                    return "Forty-Love"
                if points_player2==1:
                    return  "Forty-Fifteen"
                return "Forty-Thirty"
        else:
            if points_player2>=4:
                if points_player2-points_player1>1:
                    return "Win for player2"
                return "Advantage player2"
            else:
                if points_player2==1:
                    return "Love-Fifteen"
                if points_player2==2:
                    if points_player1==0:
                        return "Love-Thirty"
                    return "Fifteen-Thirty"
                if points_player1==0:
                    return "Love-Forty"
                if points_player1==1:
                    return  "Fifteen-Forty"
                return "Thirty-Forty"                

    def won_point(self, player:Player)->None:
        if self.player1.is_equal(player):
            self.player1.add_point()
            print (self.player1.get_points())
        else:
            self.player2.add_point()
