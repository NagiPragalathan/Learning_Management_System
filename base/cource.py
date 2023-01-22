# from ..Chatbot import chatbot
import requests
from bs4 import BeautifulSoup
from bing_image_downloader import downloader
import os
from django.shortcuts import render

# from ...models import FilesUpload
def Cscrping(Text, paraLen,Tags):
        
        def url(query): # this function generateing a links
            links : list = []
            try:
                from googlesearch import search
            except ImportError:
                print("No module named 'google' found")
            # to search
            try:           
                for j in search(query, num_results=paraLen):
                    links.append(j)
            except:
                return "Problem occers in link generator(to search)"
            return links

        # link for extract html data
        def getdata(url):
            try:
                r = requests.get(url)
                return r.text
            except:
                return "none"
        link : list = url(Text) #total links

        output : list = []
        data : str = "" 
        for i in range(paraLen):
            htmldata = getdata(link[i])
            soup = BeautifulSoup(htmldata, 'html.parser')
            data : str = ''
            for data in soup.find_all(Tags):
                output.append(data.get_text())
        print(output)
        return output


def KeyWordToimage(Keyword, limit, dir_name):
    arr = Keyword.split(",")
    for i in range(len(arr)):
        downloader.download(arr[i], limit=limit,  output_dir=dir_name, 
        adult_filter_off=True, force_replace=False, timeout=60)
def create_page(Search):
    def url(query): # this function generateing a links
                links : list = []
                try:
                    from googlesearch import search
                except ImportError:
                    print("No module named 'google' found")
                # to search
                try:           
                    for j in search(query, num_results=100):
                        links.append(j)
                except:
                    return "Problem occers in link generator(to search)"
                return links

    search = Search
    link = url(search)
    links = ""
    path = "C:/Users/NagiPragalathan/Desktop/FarmTech/Main/templates/cources/school_education"
    contant = Cscrping(search,5,"p")
    head = Cscrping(search,18,"h1")
    Code = ""
    new="C:/Users/NagiPragalathan/Desktop/SyudyKit/StudyKit/static/cources/school_education"
    KeyWordToimage(search,13,"C:/Users/NagiPragalathan/Desktop/SyudyKit/StudyKit/static/cources/school_education")

    Code = Code + "<h1>" + search +"</h1>"
    y = 4
    count = 0
    files = open(f"{path}/simple.html","w",encoding='utf-8')
    file = os.listdir(f"{new}/"+search)

    for i in link:
        links = links + f"<a href='{i}'>" + i + "</a></br>" 
    fullcontant = ""
    for i in contant[13:]:
        fullcontant = fullcontant + i + "</br>"

    html = f"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <!--
    Template Name: {search}
    ~~% load static %!!!
    
    Author: <a href="http://www.os-templates.com/">OS Templates</a>
    Author URI: http://www.os-templates.com/
    Licence: Free to use under our free template licence terms
    Licence URI: http://www.os-templates.com/template-terms
    -->
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <title>{search}</title>
    <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
    <link rel="stylesheet" href="~~% static 'cources/school_education/layout/styles/layout.css' %!!!" type="text/css" />
    <script type="text/javascript" src="~~% static 'cources/school_education/layout/scripts/jquery.min.js' %!!!"></script>
    <script type="text/javascript" src="~~% static 'cources/school_education/layout/scripts/jquery.slidepanel.setup.js' %!!!"></script>
    <!-- Homepage Only Scripts -->
    <script type="text/javascript" src="~~% static 'cources/school_education/layout/scripts/jquery.cycle.min.js' %!!!"></script>
    <script type="text/javascript">
    $(function() ~~
        $('#featured_slide').after('<div id="fsn"><ul id="fs_pagination">').cycle(~~
            timeout: 5000,
            fx: 'fade',
            pager: '#fs_pagination',
            pause: 1,
            pauseOnPagerHover: 0
        !!!);
    !!!);
    </script>
    <!-- End Homepage Only Scripts -->
    </head>
    <body>
    <div class="wrapper col0">
    <div id="topbar">
        <div id="slidepanel">
        <div class="topbox">
            <h2>Nullamlacus dui ipsum</h2>
            <p>Nullamlacus dui ipsum conseque loborttis non euisque morbi penas dapibulum orna. Urnaultrices quis curabitur phasellentesque congue magnis vestibulum quismodo nulla et feugiat. Adipisciniapellentum leo ut consequam ris felit elit id nibh sociis malesuada.</p>
            <p class="readmore"><a href="#">Continue Reading &raquo;</a></p>
        </div>
        <div class="topbox">
            <h2>Teachers Login Here</h2>
            <form action="#" method="post">
            <fieldset>
                <legend>Teachers Login Form</legend>
                <label for="teachername">Username:
                <input type="text" name="teachername" id="teachername" value="" />
                </label>
                <label for="teacherpass">Password:
                <input type="password" name="teacherpass" id="teacherpass" value="" />
                </label>
                <label for="teacherremember">
                <input class="checkbox" type="checkbox" name="teacherremember" id="teacherremember" checked="checked" />
                Remember me</label>
                <p>
                <input type="submit" name="teacherlogin" id="teacherlogin" value="Login" />
                &nbsp;
                <input type="reset" name="teacherreset" id="teacherreset" value="Reset" />
                </p>
            </fieldset>
            </form>
        </div>
        <div class="topbox last">
            <h2>Pupils Login Here</h2>
            <form action="#" method="post">
            <fieldset>
                <legend>Pupils Login Form</legend>
                <label for="pupilname">Username:
                <input type="text" name="pupilname" id="pupilname" value="" />
                </label>
                <label for="pupilpass">Password:
                <input type="password" name="pupilpass" id="pupilpass" value="" />
                </label>
                <label for="pupilremember">
                <input class="checkbox" type="checkbox" name="pupilremember" id="pupilremember" checked="checked" />
                Remember me</label>
                <p>
                <input type="submit" name="pupillogin" id="pupillogin" value="Login" />
                &nbsp;
                <input type="reset" name="pupilreset" id="pupilreset" value="Reset" />
                </p>
            </fieldset>
            </form>
        </div>
        <br class="clear" />
        </div>
        <div id="loginpanel">
        <ul>
            <li class="left">Log In Here &raquo;</li>
            <li class="right" id="toggle"><a id="slideit" href="#slidepanel">Administration</a><a id="closeit" style="display: none;" href="#slidepanel">Close Panel</a></li>
        </ul>
        </div>
        <br class="clear" />
    </div>
    </div>
    <!-- ####################################################################################################### -->
    <div class="wrapper col1">
    <div id="header">
        <div id="logo">
        <h1><a href="index.html">{search}</a></h1>
        <p>results for {search}</p>
        </div>
        <div id="topnav">
        <ul>
            <li class="active"><a href="index.html">Results</a></li>
            <li><a href=" ">Home</a></li>
        </ul>
        </div>
        <br class="clear" />
    </div>
    </div>
    <!-- ####################################################################################################### -->
    <div class="wrapper col2">
    <div id="featured_slide">
        <div class="featured_box"><a href="#"><img src="~~% static 'cources/school_education/{search}/{file[0]}' %!!!" alt="" /></a>
        <div class="floater">
            <h2>{head[0]}</h2>
            <p>{contant[0]}</p>
            <p class="readmore"><a href="#">Continue Reading &raquo;</a></p>
        </div>
        </div>
        <div class="featured_box"><a href="#"><img src="~~% static 'cources/school_education/{search}/{file[1]}' %!!!" alt="" /></a>
        <div class="floater">
            <h2>{head[1]}</h2>
            <p>{contant[1]}</p>
            <p class="readmore"><a href="#">Continue Reading &raquo;</a></p>
        </div>
        </div>
        <div class="featured_box"><a href="#"><img src="~~% static 'cources/school_education/{search}/{file[2]}' %!!!" alt="" /></a>
        <div class="floater">
            <h2>{head[2]}</h2>
            <p>{contant[2]}</p>
            <p class="readmore"><a href="#">Continue Reading &raquo;</a></p>
        </div>
        </div>
        <div class="featured_box"><a href="#"><img src="~~% static 'cources/school_education/{search}/{file[3]}' %!!!" alt="" /></a>
        <div class="floater">
            <h2>{head[3]}</h2>
            <p>{contant[3]}</p>
            <p class="readmore"><a href="#">Continue Reading &raquo;</a></p>
        </div>
        </div>
        <div class="featured_box"><a href="#"><img src="~~% static 'cources/school_education/images/demo/450x300.gif' %!!!"  alt="" /></a>
        <div class="floater">
            <h2>{head[4]}</h2>
            <p>{contant[4]}</p>
            <p class="readmore"><a href="#">Continue Reading &raquo;</a></p>
        </div>
        </div>
    </div>
    </div>
    <!-- ####################################################################################################### -->
    <div class="wrapper col3">
    <div id="homecontent">
        <div class="fl_left">
        <div class="column2">
            <ul>
            <li>
                <h2>{head[11]}</h2>
                <div class="imgholder"><img src="~~% static 'cources/school_education/{search}/{file[3]}' %!!!" alt="" /></div>
                <p>{contant[6]}</p>
                <p>{contant[7]}</p>
                <p class="readmore"><a href="#">Continue Reading &raquo;</a></p>
            </li>
            <li class="last">
                <h2>{head[12]}</h2>
                <div class="imgholder"><img src="~~% static 'cources/school_education/{search}/{file[12]}' %!!!" alt="" /></div>
                <p>{contant[8]}</p>
                <p>{contant[9]}</p>
            
                <p class="readmore"><a href="#">Continue Reading &raquo;</a></p>
            </li>
            </ul>
            <br class="clear" />
        </div>
        <div class="column2">
            <h2>About {search}</h2>
            <img class="imgl" src="~~% static 'cources/school_education/{search}/{file[4]}' %!!!" alt="" />
            <p>{contant[10]}</p>
            <p>{contant[11]}</p>
            <p>{contant[12]}</p>
            <p>{fullcontant}</p>
        </div>
        </div>
        <div class="fl_right">
        <h2>Latest From The School Blog</h2>
        <ul>
            <li>
            <div class="imgholder"><a href="#"><img src="~~% static 'cources/school_education/{search}/{file[5]}' %!!!" alt="" /></a></div>
            <p><strong><a href="#">{head[5]}</a></strong></p>
            <p>{contant[14]}</p>
            </li>
            <li>
            <div class="imgholder"><a href="#"><img src="~~% static 'cources/school_education/{search}/{file[6]}' %!!!" alt="" /></a></div>
            <p><strong><a href="#">{head[6]}</a></strong></p>
            <p>{contant[15]}</p>
            </li>
            <li>
            <div class="imgholder"><a href="#"><img src="~~% static 'cources/school_education/{search}/{file[7]}' %!!!" alt="" /></a></div>
            <p><strong><a href="#">{head[7]}</a></strong></p>
            <p>{contant[16]}</p>
            </li>
            <li>
            <div class="imgholder"><a href="#"><img src="~~% static 'cources/school_education/{search}/{file[8]}' %!!!" alt="" /></a></div>
            <p><strong><a href="#">{head[8]}</a></strong></p>
            <p>{contant[17]}</p>
            </li>
            <li class="last">
            <div class="imgholder"><a href="#"><img src="~~% static 'cources/school_education/{search}/{file[9]}' %!!!" alt="" /></a></div>
            <p><strong><a href="#">{head[9]}</a></strong></p>
            <p>{contant[18]}</p>
            </li>
            <li class="last">
            <div class="imgholder"><a href="#"><img src="~~% static 'cources/school_education/{search}/{file[9]}' %!!!" alt="" /></a></div>
            <p><strong><a href="#">{head[9]}</a></strong></p>
            <p>{links}</p>
            </li>
        </ul>
        </div>
        <br class="clear" />
    </div>
    </div>
    </body>
    </html>"""


    html = "{".join(html.split("~~"))
    html = "}".join(html.split("!!!"))


    # Code = Code + f"<img src = '{file[0]}' %!!!' class='img'>"
    # for x,i in enumerate(contant):
    #     if(x == y):
    #         y = y + 7
    #         try:
    #             Code = Code + f"<img src = '{file[cou' %!!!nt+1]}' class='img'>"
    #         except:
    #             pass
    #         count = count + 1
    #     Code = Code + i + "</br>"
        
    # print(Code)
    files.writelines(html)
    print("writed")
    files.close()

def Agri(request):
    inp_value = request.GET.get('inp') 
    create_page(inp_value)
    return render(request, 'cources/school_education/simple.html')
