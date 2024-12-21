#include <iostream>

int main()
{
    const char PLAYER = 'X';
    const char ENEMY = 'O';
    const char SPACE = '-';

    char board00, board01, board02;
    char board10, board11, board12;
    char board20, board21, board22;
    std::cin >> board00 >> board01 >> board02
             >> board10 >> board11 >> board12
             >> board20 >> board21 >> board22;

    std::cout << "+-+-+-+\n"
              << '|' << board00 << '|' << board01 << '|' << board02 << "|\n"
              << "+-+-+-+\n"
              << '|' << board10 << '|' << board11 << '|' << board12 << "|\n"
              << "+-+-+-+\n"
              << '|' << board20 << '|' << board21 << '|' << board22 << "|\n"
              << "+-+-+-+\n";

    int row = -1, col = -1;

    if (board00 == SPACE && board01 == PLAYER && board02 == PLAYER)
    {
        // Take (0, 0) for a winning row 0
        row = 0;
        col = 1;
    }
    else
    {
        if (board00 == PLAYER && board01 == SPACE && board02 == PLAYER)
        {
            // Take (0, 1) for a winning row 0
            row = 0;
            col = 2;
        }
        // MORE CODE HERE
    }

    std::cout << row << ' ' << col << std::endl;

    return 0;
}
\end{console}
}
