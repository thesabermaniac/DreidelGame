import dreidel


class DreidelGame:

    def __init__(self):
        self.__dreidel = dreidel.Dreidel()
        self.__player_names = []
        self.__player_scores = []
        self.__num_players = 0
        self.__START_SCORE = 0
        self.__winning_score = 5

    def init_game(self):
        self.__num_players = int(input("How many players are playing? "))
        for p in range(self.__num_players):
            name = input("What is the name of Player " + str(p+1) + "? ")
            self.__player_names.append(name)
            self.__player_scores.append(self.__START_SCORE)

    def player_spin(self):
        for p in range(len(self.__player_names)):
            input(self.__player_names[p] + ", press Enter when you're ready to spin. ")
            spin = self.__dreidel.spin()
            if spin == 0:
                print("You spun a Nun.")
            elif spin == 1:
                print("You spun a Gimmel.")
                self.__player_scores[p] += 2
            elif spin == 2:
                print("You spun a Hei.")
                self.__player_scores[p] += 1
            else:
                print("You spun a Shin.")
                self.__player_scores[p] -= 1

    def check_for_winner(self):
        for p in range(len(self.__player_names)):
            if self.__player_scores[p] >= self.__winning_score \
                and self.__player_scores[p] == max(self.__player_scores) \
                    and self.__player_scores.count(self.__player_scores[p]) == 1:
                print(self.__player_names[p], "wins!")
                return True
            elif self.__player_scores[p] >= self.__winning_score \
                    and self.__player_scores[p] != max(self.__player_scores) \
                    and self.__player_scores.count(max(self.__player_scores) == 1):
                winner = self.__player_scores.index(max(self.__player_scores))
                print(self.__player_names[winner], "wins!")
                return winner

    def check_for_tie(self):
        for p in range(len(self.__player_names)):
            if (self.__player_scores[p] >= self.__winning_score
                    and self.__player_scores[p] == max(self.__player_scores)
                    and self.__player_scores.count(self.__player_scores[p]) > 1) \
                    or (self.__player_scores[p] >= self.__winning_score
                        and self.__player_scores[p] != max(self.__player_scores)
                        and self.__player_scores.count(max(self.__player_scores)) > 1):
                return True

    def tie_breaker(self):
        tying_players_indices = [i for i, x in enumerate(self.__player_scores) if x == max(self.__player_scores)]
        tying_players = [self.__player_names[i] for i in tying_players_indices]
        self.__player_names.clear()
        self.__player_names.extend(tying_players)
        self.__player_scores.clear()
        for p in range(len(self.__player_names)):
            self.__player_scores.append(self.__START_SCORE)
        print("There is a tie between", " and ".join([', '.join(self.__player_names[:-1]), self.__player_names[-1]]))
        print("Here are the rules for a tie-breaker: ",
              ' and '.join([', '.join(self.__player_names[:-1]), self.__player_names[-1]]),
              "will spin again. Whoever gets the higher roll wins!!")
        self.__winning_score = max(self.__player_scores)
        self.check_for_tie()

    def __str__(self):
        scores = ''
        for i in range(len(self.__player_names)):
            scores += str(self.__player_names[i]) + ': ' + str(self.__player_scores[i]) + '\n'
        return scores
