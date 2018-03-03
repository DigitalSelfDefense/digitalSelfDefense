#!/usr/bin/env python
import glob
import os

categories_dir = 'categories/*'
categories=glob.glob(categories_dir)
for category_path in categories:
    category_name  = category_path.split('/')[1]
    category_filename = category_path + '/readme.md'
    f = open(category_filename, 'r+')
    write_str = '---\nlayout: category\ntitle: \"Category: ' + category_name + '\"\ncategory: ' + category_name + '\npermalink: /' + category_name + '\nrobots: noindex\n---\n'
    f.write(write_str)
    f.close()

    pages=glob.glob(category_path + '/*/')
    # for page_path in pages:
    #     page_name = page_path.split('/')[2]
    #     print page_name
    #     f = open(page_path)
    #     crawl = False
    #     for line in f:
    #         if crawl:
    #             current_categories = line.strip().split()
    #             if current_categories[0] == 'permalink:':
    #                 line.
    #                 total_categories.extend(current_categories[1:])
    #                 crawl = False
    #                 break
    #         if line.strip() == '---':
    #             if not crawl:
    #                 crawl = True
    #             else:
    #                 crawl = False
    #                 break
        
    # for line in f:
    # if not "tom" in line:
    #     output.append(line)
    # f.close()
    # f = open(fn, 'w')
    # f.writelines(output)
    # f.close()
