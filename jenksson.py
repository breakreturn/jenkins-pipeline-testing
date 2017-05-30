#!/bin/python

from subprocess import call
import subprocess
import sys


def get_crumb():
    crumb = subprocess.check_output([
        "curl",
        "-u",
        "admin:admin",
        "-s",
        "http://USER:TOKEN@localhost:8080/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,\":\",//crumb)"])

    return crumb


def get_job_template(crumb):
    config = subprocess.check_output([
        "curl",
        "-H",
        crumb,
        "-X",
        "GET",
        "http://admin:admin@localhost:8080/job/empty-pipeline-job/config.xml"])

    return config


def create_job(crumb, config, job_name):
    res = subprocess.check_output([
        "curl",
        "-s",
        "-H",
        crumb,
        "-X",
        "POST",
        "http://admin:admin@localhost:8080/createItem?name=Dynamic-job-" + job_name,
        "--data-binary",
        config,
        "-H",
        "Content-Type:text/xml"])


def delete_job(crumb, job_name):
    res = subprocess.check_output([
        "curl",
        "-s",
        "-H",
        crumb,
        "-X",
        "POST",
        "http://admin:admin@localhost:8080/job/Dynamic-job-" + job_name + "/doDelete"])

    print res


def run_job(crumb, job_name):
    res = subprocess.check_output([
        "curl",
        "-u",
        "admin:admin",
        "-H",
        crumb,
        "-X",
        "POST",
        "http://localhost:8080/job/Dynamic-job-" + job_name + "/build?delay=0sec"])

    print res



if __name__ == "__main__":
    crumb = get_crumb()
    job_template = get_job_template(crumb)

    job_name = sys.argv[1]

    if len(sys.argv) == 3:
        command = sys.argv[2]
        if command == "delete":
            delete_job(crumb, job_name)
        elif command == "run":
            run_job(crumb, job_name)
        elif command == "create":
            create_job(crumb, job_template, job_name)
    else:
        print "Usage: python jenksson.py <job-name> <command>"
        print "Commands: create, run, delete"

    print "Done from Jenksson"

