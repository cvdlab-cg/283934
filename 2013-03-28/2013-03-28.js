function Point2D (x,y){
	this.x = x;
	this.y = y;
}

function Edge (u,v){
	this.u = u;
	this.v = v;
}

function Triangle(a,b,c){
	this.a = a;
	this.b = b;
	this.c = c;
	
	this.area = function(){
		var e1 = new Edge(a,b); 
		var e2 = new Edge(b,c);
		var e3 = new Edge(a,c);
		var p = this.perimeter()/2;
		return Math.sqrt(p*(p-e1.length())*(p-e2.length())*(p-e3.length()));
	};
}


//add length to Edge
Edge.prototype.length = function() {return Math.sqrt(Math.pow((this.v.x-this.u.x),2)+Math.pow((this.v.y-this.u.y),2));};

//add perimeter to Triangle
Triangle.prototype.perimeter = function() {return this.a.length()+this.b.length()+this.c.length();};

//add area to Triangle
Triangle.prototype.area = function() {var p = this.perimeter()/2; return Math.sqrt(p*(p-this.a.length())*(p-this.b.length())*(p-this.c.length()));};
