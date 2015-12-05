#include <iostream>
#include <iomanip>
#include <string>
#include <ctime>
#include <queue>
 
using namespace std;
 
//make a grid based node class
class Node{
public:
    Node(int value, int x_coord, int y_coord){
        _value = value;
        _x_coord = x_coord;
        _y_coord = y_coord;
        _down = nullptr;
        _right = nullptr;
    }
    ~Node();
     
    int value() const{return _value;}
    void set_value(int value) {_value = value;}
     
    int x_coord(){return _x_coord;}
    int y_coord(){return _y_coord;}
     
    Node* right() const{return _right;}
    void set_right(Node* right){_right = _right;}
     
    Node* down() const{return _down;}
    void set_down(Node* down){_down = _down;}
     
private:
    int _value, _x_coord, _y_coord;
    Node *_right, *_down;
};
class Maze{
public:
//===================================================================================
//Constructor, Destructor
//===================================================================================
    Maze(int width, int height, int density){
        _width = width;
        _height = height;
        _density = density;
        _size = 0;
        generate_map();
    }
    ~Maze(){clear();}
//===================================================================================
//Functions for Destructor: empty(), pop(), clear()
//===================================================================================
    bool empty() const{return _size == 0;}
    void pop(Node *node){
        //if there is a node to the right, move along to the right
        if(node->right()!=nullptr)
			pop(node->right());
        //if there isn't a not to the right, try going down
        else if(node->right()==nullptr){
            //if there is a node below, move along downward
            if(node->down()!=nullptr){
                pop(node->down());
            //if there isn't a not downward, pop it
            }else if(node->down()==nullptr){
                delete node;
				_size--;
			}
        }
    }
    void clear(){
			while(!empty())
				pop(_origin);
		}
//===================================================================================
//Variable Set and Get Functions (removed set and made maze a one-time use per call)
//===================================================================================
    int width() const{return _width;}
//  void set_width(int width){_width = width;}
    int height() const{return _height;}
//  void set_height(int height){_height = height;}
    int density() const{return _density;}
//  void set_density(int density){_density = density;}
    Node *start(){return _start;}
    Node *finish(){return _finish;}
//===================================================================================
//Base Map Generator: create the plane
//===================================================================================
    void generate_map(){
        srand(time(NULL));
        int space;
        if(_origin==nullptr){
            if(rand()%100 < _density){
                //wall
                space = 1;
            }else{
                //space
                space = 0;
            }
            _origin = new Node(space, 1, 1);
        }
        add_x_node(_origin);
        //set starting point
        _start = iterator(1, (rand()%_height + 1));
		_start->set_value(0);
        //set finishing point
        _finish = iterator(_width, (rand()%_height + 1));
		_finish->set_value(0);
    }
//===================================================================================
//Iterator
//===================================================================================
    Node* iterator(int x, int y){
        return y_iter(x_iter(_origin, x), y);
    }
//===================================================================================
//Print
//===================================================================================   
    void print(){
        int read;
        for(int i = 0; i <= _width+1; i++)
            cout << 'X';
        cout << endl;
        for(int j = 1; j <= _height; j++){
            cout << 'X';
            for(int i = 1; i <= _width; i++){
                read = iterator(i, j)->value();
                switch(read){
                    case 0:
                        cout << ' ';
                        break;
                    case 1:
                        cout << 'X';
                        break;
                    case 2:
                        cout << '*';
                        break;
                }
            }
        cout << 'X' << endl;
        }
        for(int i = 0; i <= _width+1; i++){
            cout << 'X';
		}
        cout << endl;
    }
private:
//===================================================================================
//Helper Functions
//===================================================================================
    void add_x_node(Node *node){
        int space;
        if(node->down()==nullptr){
            add_y_node(node);
        }
        if(node->x_coord() != _width){
            if(rand()%100 < _density){
                space = 1;
            }else{
                space = 0;
            Node *new_node = new Node(space, node->x_coord() + 1, 0);
            node->set_right(new_node);
            _size++;
            add_x_node(new_node);
			}
		}
    }
    void add_y_node(Node *node){
        int space;
		Node *new_node;
        if(node->y_coord() != _height){
            if(rand()%100 < _density){
                space = 1;
            }else{
                space = 0;
            new_node = new Node(space, node->x_coord(), node->y_coord() + 1);
            node->set_down(new_node);
            _size++;
            add_y_node(new_node);
			}
		}
	}
    Node* x_iter(Node *node, int x){
        if(x != 0){
            return x_iter(node->right(), x--);
        }
        else if(x == 0){
            return node;
        }
    }
    Node* y_iter(Node *node, int y){
        if(y != 0){
            return y_iter(node->down(), y--);
        }
        else if(y == 0){
            return node;
        }
    }
    int _width, _height, _density, _size;
    Node *_origin, *_start, *_finish;
};

class Tnode{
public:
    Tnode(Node *value){
        _value = value;
        _prev = nullptr;
    }
    ~Tnode(){}
    void set_prev(Tnode *node){
        _prev = node;
    }
    Tnode *prev(){
        return _prev;
    }
    Node *value(){
        return _value;
    }
private:
    Tnode *_prev;
    Node *_value;
};

class Mouse{
public:
    Mouse(Maze *maze){
        _root = nullptr;
        _shortest = nullptr;
        _finished = false;
		_maze = maze;
        solve();
    }
    ~Mouse();
    bool finish(){return _finished;}
    void solve(){
        Tnode *active_node;
        if(_root == nullptr){
            _root = new Tnode(_maze->start());
            _maze->start()->set_value(2);
        }
        _queuednode.push(_root);
        do{
            active_node = _queuednode.front();
            _queuednode.pop();
            search(active_node);
        }while(_queuednode.size() != 0);
        if(_finishnode.size() > 0)
            _finished = true;
    }
    void search(Tnode *node){
        //right
		Tnode *new_node;
        if(_maze->iterator(node->value()->x_coord()+1,node->value()->y_coord())->value() == 0){
			//maze -> iterated node -> setting its value
            _maze->iterator(node->value()->x_coord()+1,node->value()->y_coord())->set_value(2);
            new_node = new Tnode(_maze->iterator(node->value()->x_coord()+1,node->value()->y_coord()));
            new_node->set_prev(node);
            if(new_node->value()->x_coord() == _maze->finish()->x_coord() && node->value()->y_coord() == _maze->finish()->y_coord())
                _finishnode.push(node);
            else
                _queuednode.push(new_node);
        }
        //up
        if(_maze->iterator(node->value()->x_coord(),node->value()->y_coord()-1)->value() == 0){
            _maze->iterator(node->value()->x_coord(),node->value()->y_coord()-1)->set_value(2);
            new_node = new Tnode(_maze->iterator(node->value()->x_coord(),node->value()->y_coord()-1));
            new_node->set_prev(node);
            if(new_node->value()->x_coord() == _maze->finish()->x_coord() && node->value()->y_coord() == _maze->finish()->y_coord())
                _finishnode.push(node);
            else
                _queuednode.push(new_node);
        }
        //down
        if(_maze->iterator(node->value()->x_coord(),node->value()->y_coord()+1)->value() == 0){
            _maze->iterator(node->value()->x_coord(),node->value()->y_coord()+1)->set_value(2);
            new_node = new Tnode(_maze->iterator(node->value()->x_coord()+1,node->value()->y_coord()));
            new_node->set_prev(node);
            if(new_node->value()->x_coord() == _maze->finish()->x_coord() && node->value()->y_coord() == _maze->finish()->y_coord())
                _finishnode.push(node);
            else
                _queuednode.push(new_node);
        }
        //left
        if(_maze->iterator(node->value()->x_coord()-1,node->value()->y_coord())->value() == 0){
            _maze->iterator(node->value()->x_coord()-1,node->value()->y_coord())->set_value(2);
            new_node = new Tnode(_maze->iterator(node->value()->x_coord()-1,node->value()->y_coord()));
            new_node->set_prev(node);
            if(new_node->value()->x_coord() == _maze->finish()->x_coord() && node->value()->y_coord() == _maze->finish()->y_coord())
                _finishnode.push(node);
            else
                _queuednode.push(new_node);
        }
    } 
    int shortestlength(){
        Tnode *active_node;
        int current_shortest = 9999999999;
        do{
            active_node = _finishnode.front();
            if(chainlength(active_node, 0) < current_shortest){
                current_shortest = chainlength(active_node, 0);
                //try to figure out for printing use
                _shortest = active_node;
            }
            _finishnode.pop();
        }while(_finishnode.size() != 0);
        return current_shortest;
    }
    int chainlength(Tnode *node, int length){
        if(node->prev() == nullptr)
            return length;
        else
            return chainlength(node->prev(), length++);
    }
private:
    Tnode *_root, *_shortest;
    bool _finished;
	Maze *_maze;
    queue<Tnode*> _queuednode, _finishnode;
};
void welcome();
void user_input(int& w, int& h, int& d);
void result(Mouse *mouse);
void shortestroute(int x);
int main(){
//Declare variable
    int width, height, density;
//Take values for width. height, and density
    user_input(width, height, density);
//Create maze
    Maze maze(width, height, density);
    maze.print();
    Mouse mouse(&maze);
    result(&mouse);
    maze.print();
}
 
void welcome();
void user_input(int& w, int& h, int& d){
    //input width
    cout << "Enter the width of the maze (1-99): ";
    cin >> w;
    cout << '\n';
    //input height
    cout << "Enter the height of the maze (1-99): ";
    cin >> h;
    cout << '\n';
    //input density
    cout << "Enter the density of the maze (1-99): ";
    cin >> d;
    cout << '\n';
}
void result(Mouse *mouse){
    if(mouse->finish()){
        cout << "The mouse have successfully cross the maze.\n";
        shortestroute(mouse->shortestlength());
    }
    else
        cout << "The mouse have failed to cross the maze.\n";
}
void shortestroute(int x){
    cout << "The shortest route took x steps\n";
}
 
