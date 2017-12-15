from flask import Flask,render_template,views,request
from crawl import get_one_page,parse_one_page,check_rank


app = Flask(__name__)

KEYWORDS = ''


@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/check/',methods=['GET','POST'])
def check():
    if request.method == 'GET':
        return render_template('check.html')
    else:
        # print(request.form.to_dict()['keyword'])
        KEYWORDS = request.form.to_dict()['keyword']
        rank = None
        for v in range(10):
            if v == 0:
                res = get_one_page('https://www.dhgate.com/w/%s.html' % KEYWORDS)
                page = parse_one_page(res)
                rank = check_rank(page)
                if rank:
                    return render_template('check.html',rank=rank)
            else:
                res = get_one_page('https://www.dhgate.com/w/%s/%s.html' % (KEYWORDS,v))
                page = parse_one_page(res)
                rank = check_rank(page)
                if rank:
                    return render_template('check.html',rank=rank)

if __name__ == '__main__':
    app.run(debug=True)
