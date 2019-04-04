FROM kbase/kb_python:latest

ADD reapNarratives.py /kb/module/

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/kbase/narrativeReaper.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="0.0.1" \
      us.kbase.vcs-branch=$BRANCH \
      maintainer="Keith Keller kkeller@lbl.gov"
