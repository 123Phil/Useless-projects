#include <iostream>
#include <queue>
#include <ctime>
#include <cstdlib>
using namespace std;

class Maze {
	//Maze is 2-D array of ints
	//  0 indicates an empty square
	//  1 indicates a wall
	//  2 indicates a path that has been traversed
	
	
	typedef struct _point {
		int x;
		int y;
	} point;
	
	
	int w,h,d;
	int **maze;
	point start,end;
	
	
public:
	Maze();
	Maze(int width, int height, int density)
	{
		w = (width < 80) ? width : 80;
		h = (height < 80) ? height : 40;
		d = (density < 100) ? density : 100;
		
		int i,j;
		
		//Add room for a border
		w += 2;
		h += 2;
		
		//create 2-d array
		maze = new int*[h];
		for (i=0; i < h; i++)
			maze[i] = new int[w];
		
		//Make border
		srand(time(NULL));
		for (i=0; i < w; i++) {
			maze[0][i] = 1;
			maze[h-1][i] = 1;
		}
		for (i=1; i < h-1; i++) {
			maze[i][0] = 1;
			maze[i][w-1] = 1;
		}
		//Set start and end points
		i = ( rand() % (h-2) ) + 1;
		start.x = 0;
		start.y = i;
		maze[i][0] = 0;
		i = ( rand() % (h-2) ) + 1;
		end.x = w-1;
		end.y = i;
		maze[i][w-1] = 0;
		
		//Add inner walls
		for (i=1; i < h-1; i++) {
			for (j=1; j < w-1; j++) {
				if ( rand()%100 >= d ) {
					maze[i][j] = 0;
				} else {
					maze[i][j] = 1;
				}
			}
		}
	}

	~Maze()
	{
		for (int i=0; i < h; i++)
			delete maze[i];
		delete [] maze;
	}

	void print()
	{
		for (int i=0; i < h; i++) {
			for (int j=0; j < w; j++) {
				if (maze[i][j] == 0)
					cout << ' ';
				else if (maze[i][j] == 1)
					cout << 'X';
				else if (maze[i][j] == 2)
					cout << '+';
				else
					cout << '@'; //if you see one of these, something went wrong
			}
			cout << endl;
		}
	}
	
	bool solve()
	{
		queue<point> points;
		points.push(start);
		point current, pusher;
		
		while (!points.empty()) {
			//enqueue neighbors, if end, return
			current = points.front();
			points.pop();

			if (current.x == end.x
			 && current.y == end.y)
				return true;

			if (current.x > 0) { //left
				if (maze[current.y][current.x-1] == 0) {
					maze[current.y][current.x-1] = 2;
					pusher.x = current.x-1;
					pusher.y = current.y;
					points.push(pusher);
				}
			}
			if (current.y > 0) { //up
				if (maze[current.y-1][current.x] == 0) {
					maze[current.y-1][current.x] = 2;
					pusher.x = current.x;
					pusher.y = current.y-1;
					points.push(pusher);
				}
			}
			if (current.x < w-1) { //right
				if (maze[current.y][current.x+1] == 0) {
					maze[current.y][current.x+1] = 2;
					pusher.x = current.x+1;
					pusher.y = current.y;
					points.push(pusher);
				}
			}
			if (current.y < h-1) { //down
				if (maze[current.y+1][current.x] == 0) {
					maze[current.y+1][current.x] = 2;
					pusher.x = current.x;
					pusher.y = current.y+1;
					points.push(pusher);
				}
			}
		}
	return false;
	}

}; //end of Maze class


void getUserInput(int &w, int &h, int &d)
{
	cout << "Enter the width of the maze (1-80): ";
	cin >> w;
	cout << "Enter the height of the maze (1-40): ";
	cin >> h;
	cout << "Enter the density of the maze (0-100): ";
	cin >> d;
	cout << '\n';
}


int main()
{//rewrite for maze class
	int w,h,d;
	getUserInput(w,h,d);

	Maze M(w,h,d);

	cout << "Here is your maze!\n";
	M.print();

	cout << "\nPress ENTER to solve.\n";
	cin.get();
	cin.get();

	if (M.solve()) {
		cout << "Solution found!\n";
		M.print();
	}
	else cout << "No solution found.\n";

	return 0;
}




