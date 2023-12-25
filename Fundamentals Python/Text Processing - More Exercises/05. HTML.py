article_title = input()
article_content = input()

print(f"<h1>\n    {article_title}\n"+"</h1>")
print(f"<article>\n    {article_content}\n"+"</article>")

article_comments = input()
while article_comments != "end of comments":
    print(f"<div>\n    {article_comments}\n"+"</div>")

    article_comments = input()
